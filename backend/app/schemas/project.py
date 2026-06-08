from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    project_name: str
    project_type: str

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    project_name: Optional[str] = None

class ProjectInDB(ProjectBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
