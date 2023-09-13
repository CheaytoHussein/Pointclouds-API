from celery import Celery


class CeleryService:

    def __init__(self):
        self.celery_worker = Celery('celery')
        json_celery_config = {}
        with open('celery_config.json', 'r') as json_data:
            json_celery_config = json_data
            print(json_celery_config)