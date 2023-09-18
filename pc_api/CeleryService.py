import json
from celery import Celery


class CeleryService:

    def __init__(self):
        self.celery_worker = Celery('celery')
        with open('/app/pc_api/celery_config.json', 'rb') as json_data:
            self.celery_worker.conf.update(json.load(json_data))

    def voxel_downsample(self, path_to_ply, voxel_size):
        return self.celery_worker.send_task(
            name="voxel",
            queue="voxel_queue",
            args=(path_to_ply, voxel_size)
        )
