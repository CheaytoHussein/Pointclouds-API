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
def add_noise():
    pass


@celery_worker.task(name="jittering", queue="jittering_queue")
def jitter():
    pass
