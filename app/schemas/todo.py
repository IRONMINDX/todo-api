from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TodoBase(BaseModel):
    title: str
    description: str | None = None
    status: str
    priority: str
    due_date: datetime | None = None


class TodoCreate(TodoBase):
    user_id: UUID


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    due_date: datetime | None = None


class TodoResponse(TodoBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)