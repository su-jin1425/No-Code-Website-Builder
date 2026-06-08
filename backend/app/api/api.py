from fastapi import APIRouter
from app.api.endpoints import builder, projects

api_router = APIRouter()
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(builder.router, prefix="/builder", tags=["builder"])
