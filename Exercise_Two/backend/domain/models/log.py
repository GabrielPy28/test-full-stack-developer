from datetime import datetime
from pydantic import BaseModel
from bson import ObjectId

class Log(BaseModel):
    id: str = ObjectId()
    timestamp: datetime = datetime.now()
    request_type: str
    request_url: str
    response_status: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }