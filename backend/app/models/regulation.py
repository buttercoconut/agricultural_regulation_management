# SQLAlchemy models for Regulation
from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

# Association tables for many-to-many relationships
regulation_region = Table(
    "regulation_region",
    Base.metadata,
    Column("regulation_id", Integer, ForeignKey("regulations.id")),
    Column("region_id", Integer, ForeignKey("regions.id")),
)

regulation_category = Table(
    "regulation_category",
    Base.metadata,
    Column("regulation_id", Integer, ForeignKey("regulations.id")),
    Column("category_id", Integer, ForeignKey("categories.id")),
)

class Regulation(Base):
    __tablename__ = "regulations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    effective_date = Column(String(10), nullable=True)  # YYYY-MM-DD
    status = Column(String(50), default="draft")

    regions = relationship("Region", secondary=regulation_region, back_populates="regulations")
    categories = relationship("Category", secondary=regulation_category, back_populates="regulations")

# Minimal Region and Category models for association
class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    regulations = relationship("Regulation", secondary=regulation_region, back_populates="regions")

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    regulations = relationship("Regulation", secondary=regulation_category, back_populates="categories")
