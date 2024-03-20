from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Optional[dict] = None

    class Config:
        orm_mode = True