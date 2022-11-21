from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import List, Optional

from api import users, sections, courses

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


app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
