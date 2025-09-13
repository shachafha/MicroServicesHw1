
from __future__ import annotations
from datetime import date, datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field
from pydantic.config import ConfigDict


class TeacherBase(BaseModel):
    """Shared fields for Teacher models."""
    first_name: str = Field(..., description="Teacher's given name", examples=["Ada"])
    last_name: str = Field(..., description="Teacher's family name", examples=["Lovelace"])
    email: Optional[EmailStr] = Field(None, description="Contact email", examples=["ada@example.edu"])
    hire_date: Optional[date] = Field(None, description="Date the teacher was hired (YYYY-MM-DD)")


class TeacherCreate(TeacherBase):
    id: UUID = Field(default_factory=uuid4, description="Teacher identifier (UUID)")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp (UTC)")

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "00000000-0000-0000-0000-000000000001",
                    "first_name": "Ada",
                    "last_name": "Lovelace",
                    "email": "ada@example.edu",
                    "hire_date": "2020-09-01",
                    "created_at": "2025-01-01T00:00:00Z"
                }
            ]
        }
    )


class TeacherRead(TeacherBase):
    id: UUID
    created_at: datetime


class TeacherUpdate(BaseModel):
    first_name: Optional[str] = Field(None, description="Update given name")
    last_name: Optional[str] = Field(None, description="Update family name")
    email: Optional[EmailStr] = Field(None, description="Update email")
    hire_date: Optional[date] = Field(None, description="Update hire date")
