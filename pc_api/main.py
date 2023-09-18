from fastapi import FastAPI

from pc_api.endpoints import router

app = FastAPI()


@app.get("/")
def health_check():
    return {
        "status_code": 200,
        "message": "pc_api working properly"
    }


app.include_router(router, prefix='/pointcloud', tags=['pointcloud'])
