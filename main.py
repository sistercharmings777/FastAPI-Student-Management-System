from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title='Fast API LMS',
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Prince the amazo",
        "email": "sistercharmings@gmail.com"
    },
    license_info={
        "name": "MIT"
    }
)

users = []


class Users(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[Users])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: Users):
    users.append(user)
    return 'success'


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The id number of the user", gt=0),
                   q: str = Query(None, max_length=5)
                   ):
    return {'user': users[id], 'query': q}
