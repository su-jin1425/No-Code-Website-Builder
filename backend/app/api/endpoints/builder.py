from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.component import ComponentCreate, ComponentInDB
from app.schemas.page import PageCreate, PageInDB

router = APIRouter()

@router.post("/pages/{project_id}", response_model=PageInDB)
def create_page(project_id: int, page: PageCreate, db: Session = Depends(get_db)):
    # Placeholder logic
    return {"id": 1, "project_id": project_id, "page_name": page.page_name, "page_slug": page.page_slug, "page_structure": []}

@router.post("/components/{page_id}", response_model=ComponentInDB)
def add_component(page_id: int, component: ComponentCreate, db: Session = Depends(get_db)):
    # Placeholder logic
    return {
        "id": "uuid-123", 
        "page_id": page_id, 
        "component_type": component.component_type, 
        "component_config": component.component_config, 
        "position_data": component.position_data
    }
