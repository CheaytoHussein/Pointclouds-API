from celery import Celery

celery_worker = Celery('celery')


@celery_worker.task(name="voxel", queue="voxel_queue")
def voxel_downsampling():
    pass


@celery_worker.task(name="noise", queue="noise_queue")
def add_noise():
    pass


@celery_worker.task(name="jittering", queue="jittering_queue")
def jitter():
    pass
