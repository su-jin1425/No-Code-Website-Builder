from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class ComponentBase(BaseModel):
    component_type: str
    component_config: Dict[str, Any] = Field(default_factory=dict)
    position_data: Dict[str, Any] = Field(default_factory=dict)

class ComponentCreate(ComponentBase):
    pass

class ComponentUpdate(ComponentBase):
    component_type: Optional[str] = None

class ComponentInDB(ComponentBase):
    id: str
    page_id: int

    class Config:
        from_attributes = True
