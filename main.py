
from __future__ import annotations

# API-first placeholder service for a School system.
# Resources: /teachers and /classes with placeholder CRUD routes to auto-generate OpenAPI.

from typing import Dict, List, Optional
from uuid import UUID

from fastapi import FastAPI, HTTPException, Path, Query, status

from models.teacher import TeacherCreate, TeacherRead, TeacherUpdate
from models.school_class import ClassCreate, ClassRead, ClassUpdate

app = FastAPI(
    title="School API (API-first)",
    description="API-first skeleton with placeholder routes for Teachers and Classes.",
    version="0.1.0",
)

# In-memory placeholders (for type hints only; routes return 501)
teachers: Dict[UUID, TeacherRead] = {}
classes: Dict[UUID, ClassRead] = {}

# --------------------------- Teacher routes ----------------------------------

@app.get(
    "/teachers",
    response_model=List[TeacherRead],
    summary="List Teachers",
    description="Placeholder route that would list teachers. Returns 501 Not Implemented.",
    tags=["Teachers"],
    responses={501: {"description": "Not Implemented"}},
)
def list_teachers(
    last_name: Optional[str] = Query(None, description="Filter by last name"),
):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.post(
    "/teachers",
    response_model=TeacherRead,
    status_code=201,
    summary="Create Teacher",
    description="Placeholder route to create a teacher. Returns 501 Not Implemented.",
    tags=["Teachers"],
    responses={501: {"description": "Not Implemented"}},
)
def create_teacher(payload: TeacherCreate):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.get(
    "/teachers/{teacher_id}",
    response_model=TeacherRead,
    summary="Get Teacher",
    description="Placeholder route to fetch a specific teacher. Returns 501 Not Implemented.",
    tags=["Teachers"],
    responses={501: {"description": "Not Implemented"}},
)
def get_teacher(teacher_id: UUID = Path(..., description="Teacher UUID")):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.put(
    "/teachers/{teacher_id}",
    response_model=TeacherRead,
    summary="Replace Teacher",
    description="Placeholder route to fully replace a teacher (PUT semantics). Returns 501 Not Implemented.",
    tags=["Teachers"],
    responses={501: {"description": "Not Implemented"}},
)
def put_teacher(teacher_id: UUID, payload: TeacherCreate):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.delete(
    "/teachers/{teacher_id}",
    status_code=204,
    summary="Delete Teacher",
    description="Placeholder route to delete a teacher. Returns 501 Not Implemented.",
    tags=["Teachers"],
    responses={501: {"description": "Not Implemented"}},
)
def delete_teacher(teacher_id: UUID):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


# --------------------------- Class routes ------------------------------------

@app.get(
    "/classes",
    response_model=List[ClassRead],
    summary="List Classes",
    description="Placeholder route that would list classes. Returns 501 Not Implemented.",
    tags=["Classes"],
    responses={501: {"description": "Not Implemented"}},
)
def list_classes(
    code: Optional[str] = Query(None, description="Filter by class code"),
    teacher_id: Optional[UUID] = Query(None, description="Filter by assigned teacher UUID"),
):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.post(
    "/classes",
    response_model=ClassRead,
    status_code=201,
    summary="Create Class",
    description="Placeholder route to create a class. Returns 501 Not Implemented.",
    tags=["Classes"],
    responses={501: {"description": "Not Implemented"}},
)
def create_class(payload: ClassCreate):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.get(
    "/classes/{class_id}",
    response_model=ClassRead,
    summary="Get Class",
    description="Placeholder route to fetch a specific class. Returns 501 Not Implemented.",
    tags=["Classes"],
    responses={501: {"description": "Not Implemented"}},
)
def get_class(class_id: UUID = Path(..., description="Class UUID")):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.put(
    "/classes/{class_id}",
    response_model=ClassRead,
    summary="Replace Class",
    description="Placeholder route to fully replace a class (PUT semantics). Returns 501 Not Implemented.",
    tags=["Classes"],
    responses={501: {"description": "Not Implemented"}},
)
def put_class(class_id: UUID, payload: ClassCreate):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.delete(
    "/classes/{class_id}",
    status_code=204,
    summary="Delete Class",
    description="Placeholder route to delete a class. Returns 501 Not Implemented.",
    tags=["Classes"],
    responses={501: {"description": "Not Implemented"}},
)
def delete_class(class_id: UUID):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="API-first placeholder")


@app.get("/", tags=["Root"])
def root():
    return {"message": "School API (API-first). See /docs for OpenAPI."}
