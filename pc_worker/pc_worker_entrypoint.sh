nohup celery -A ./pc_worker.celery_worker.celery_worker worker -Q voxel_queue --loglevel=info
nohup celery -A ./pc_worker.celery_worker.celery_worker worker -Q noise_queue --loglevel=info
nohup celery -A ./pc_worker.celery_worker.celery_worker worker -Q jittering_queue --loglevel=info
