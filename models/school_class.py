
from __future__ import annotations
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class ClassBase(BaseModel):
    """Shared fields for School Class models."""
    code: str = Field(..., description="Class code (e.g., MATH101)")
    title: str = Field(..., description="Class title", examples=["Introduction to Algorithms"])
    room: Optional[str] = Field(None, description="Room where the class meets", examples=["Bldg A - 204"])
    teacher_id: Optional[UUID] = Field(None, description="UUID of the assigned teacher")


class ClassCreate(ClassBase):
    id: UUID = Field(default_factory=uuid4, description="Class identifier (UUID)")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp (UTC)")

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "00000000-0000-0000-0000-0000000000ab",
                    "code": "CS101",
                    "title": "Intro to CS",
                    "room": "Main-101",
                    "teacher_id": "00000000-0000-0000-0000-000000000001",
                    "created_at": "2025-01-01T00:00:00Z"
                }
            ]
        }
    )


class ClassRead(ClassBase):
    id: UUID
    created_at: datetime


class ClassUpdate(BaseModel):
    code: Optional[str] = None
    title: Optional[str] = None
    room: Optional[str] = None
    teacher_id: Optional[UUID] = None
