from fastapi import APIRouter
from domain.models.user import User
from domain.models.log import Log
from infrastructure.external_apis.jsonplaceholder import jsonplaceholder_api
from infrastructure.persistence.mongodb.logs_repository import LogsRepository

logs_repository = LogsRepository()

users_router = APIRouter()

@users_router.get("/users", response_model=list[User])
def get_users():
    logs_repository.save_log(Log(request_type="GET", request_url="/users", response_status=200))
    return jsonplaceholder_api.get_users()

@users_router.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    logs_repository.save_log(Log(request_type="GET", request_url=f"/users/{user_id}", response_status=200))
    return jsonplaceholder_api.get_user_by_id(user_id)