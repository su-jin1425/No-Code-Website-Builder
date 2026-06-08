from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    projects = relationship("Project", back_populates="owner")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_name = Column(String, index=True)
    project_type = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="projects")
    pages = relationship("Page", back_populates="project")

class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    page_name = Column(String)
    page_slug = Column(String, index=True)
    page_structure = Column(JSON, default=list) # Optional pre-computed tree
    created_at = Column(DateTime, default=datetime.utcnow)
    
    project = relationship("Project", back_populates="pages")
    components = relationship("Component", back_populates="page")

class Component(Base):
    __tablename__ = "components"
    id = Column(String, primary_key=True, index=True) # UUID for components
    page_id = Column(Integer, ForeignKey("pages.id"))
    component_type = Column(String, index=True)
    component_config = Column(JSON, default=dict)
    position_data = Column(JSON, default=dict)
    
    page = relationship("Page", back_populates="components")
