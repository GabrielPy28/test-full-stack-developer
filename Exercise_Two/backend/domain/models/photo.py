from pydantic import BaseModel
from typing import Optional

class Photo(BaseModel):
    id: int
    albumId: int
    title: str
    url: str
    thumbnailUrl: Optional[str] = None

    class Config:
        orm_mode = True