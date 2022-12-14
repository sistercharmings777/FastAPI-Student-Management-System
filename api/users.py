from typing import List, Optional
import fastapi
from pydantic import BaseModel


router = fastapi.APIRouter()

users = []


class Users(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/users", response_model=List[Users])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: Users):
    users.append(user)
    return 'success'


@router.get("/users/{id}")
async def get_user(id: int):
    return {'user': users[id]}
