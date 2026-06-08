from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class PageBase(BaseModel):
    page_name: str
    page_slug: str

class PageCreate(PageBase):
    pass

class PageUpdate(PageBase):
    page_name: Optional[str] = None
    page_slug: Optional[str] = None
    page_structure: Optional[List[Dict[str, Any]]] = None

class PageInDB(PageBase):
    id: int
    project_id: int
    page_structure: List[Dict[str, Any]]

    class Config:
        from_attributes = True
