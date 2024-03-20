from fastapi import APIRouter
from domain.models.photo import Photo
from domain.models.log import Log
from infrastructure.external_apis.jsonplaceholder import jsonplaceholder_api
from infrastructure.persistence.mongodb.logs_repository import LogsRepository

photos_router = APIRouter()
logs_repository = LogsRepository()

@photos_router.get("/photos/{user_id}", response_model=list[Photo])
def get_photos_by_user_id(user_id: int):
    logs_repository.save_log(Log(request_type="GET", request_url=f"/photos/{user_id}", response_status=200))
    return jsonplaceholder_api.get_photos_by_user_id(user_id)