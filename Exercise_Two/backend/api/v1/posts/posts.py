from fastapi import APIRouter
from domain.models.post import Post
from domain.models.log import Log
from infrastructure.external_apis.jsonplaceholder import jsonplaceholder_api
from infrastructure.persistence.mongodb.logs_repository import LogsRepository

logs_repository = LogsRepository()
posts_router = APIRouter()

@posts_router.get("/post/{user_id}", response_model=list[Post])
def get_posts_by_user_id(user_id: int):
    logs_repository.save_log(Log(request_type="GET", request_url=f"/posts/{user_id}", response_status=200))
    return jsonplaceholder_api.get_posts_by_user_id(user_id)