from fastapi import APIRouter
from domain.models.log import Log
from infrastructure.persistence.mongodb.logs_repository import LogsRepository

logs_router = APIRouter()
logs_repository = LogsRepository()

@logs_router.get("/logs", response_model=list[Log])
def get_logs():
    return logs_repository.get_logs()