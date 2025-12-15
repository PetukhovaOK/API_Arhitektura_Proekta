from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class UserResponse(BaseModel):

    email: str
    name: str
    nickname: str
    avatar_url: Optional[str] = None
    uuid: UUID