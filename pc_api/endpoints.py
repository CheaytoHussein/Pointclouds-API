from fastapi import APIRouter

from pc_api.CeleryService import CeleryService

router = APIRouter()
celery_service = CeleryService()


@router.post("/augment/voxel_downsampling")
def augment_pointcloud(path_to_ply: str, voxel_size: float):
    return celery_service.voxel_downsample(path_to_ply, voxel_size)
