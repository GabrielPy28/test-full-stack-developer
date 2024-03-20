from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    id: int
    userId: int
    title: str
    body: str
