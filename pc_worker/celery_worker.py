from random import random

import numpy as np
import open3d as o3d
import json
from celery import Celery

celery_worker = Celery('celery')
with open('celery_config.json', 'rb') as json_data:
    celery_worker.conf.update(json.load(json_data))


@celery_worker.task(name="voxel", queue="voxel_queue", max_retries=3)
def voxel_downsampling(pointcloud_path: str, voxel_size: float):
    pcd = o3d.io.read_point_cloud(pointcloud_path)
    pcd = pcd.voxel_down_sample(voxel_size=voxel_size)
    o3d.io.write_point_cloud(pointcloud_path, pcd)
    return {
        "status_code": 200,
        "message": "voxel downsampling done, check the file in the same path"
    }


@celery_worker.task(name="noise", queue="noise_queue")
def add_noise(ply_path: str, noise_range: int):
    pcd = o3d.io.read_point_cloud(ply_path)

    pcd_points = np.asarray(pcd.points)
    pcd_points_length, _ = pcd_points.shape
    for point, index in zip(pcd_points, range(pcd_points_length)):
        pcd_points[index] = [
            coordinate + (((-1) ** round(random())) * round(random() * noise_range))
            for coordinate in pcd_points[index]
        ]

    pcd.points = o3d.utility.Vector3dVector(pcd_points)
    o3d.io.write_point_cloud(ply_path, pcd)

    # to visualize the model
    # pcd.paint_uniform_color([0.5, 0.5, 0.5])
    # o3d.visualization.draw_geometries([pcd])


@celery_worker.task(name="jittering", queue="jittering_queue")
def jitter(ply_path: str, jitter_percentage):
    pcd = o3d.io.read_point_cloud(ply_path)
    pcd_points = np.asarray(pcd.points)
    pcd_points_length, _ = pcd_points.shape

    jitter_number = int((jitter_percentage * pcd_points_length) / 100)
    random_seed = int(random() * (pcd_points_length - jitter_number))
    print(len(pcd_points[random_seed:(random_seed + jitter_number)]))
    np.random.shuffle(pcd_points[random_seed:(random_seed + jitter_number)])
    print(len(pcd_points[random_seed:(random_seed + jitter_number)]))

    pcd.points = o3d.utility.Vector3dVector(pcd_points)
    o3d.io.write_point_cloud(ply_path, pcd)



