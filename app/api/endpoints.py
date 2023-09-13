from enum import Enum
from fastapi import APIRouter

from app.worker.CeleryService import CeleryService

router = APIRouter()
celery_service = CeleryService()


class AugmentationType(Enum):
    VOXEL_DOWNSAMPLING = "voxel_downsampling"
    ADD_NOISE = "add_noise"
    JITTERING = "jittering"


@router.get("/")
def health_check():
    return {
        "status_code": 200,
        "message": "api working properly"
    }


@router.post("/augment")
def augment_pointcloud(augmentation_type: AugmentationType, path_to_ply: str, ):
    pass
