from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.models.todo import Todo
from app.repositories.todo_repository import TodoRepository
from app.services.todo_service import TodoService

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


def get_service(db: Session):
    repository = TodoRepository(db)
    return TodoService(repository)


@router.post("/", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    service = get_service(db)

    todo_model = Todo(
        **todo.model_dump()
    )

    return service.create_todo(todo_model)


@router.get("/", response_model=list[TodoResponse])
def get_all_todos(
    db: Session = Depends(get_db)
):
    service = get_service(db)
    return service.get_all_todos()


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: UUID,
    db: Session = Depends(get_db)
):
    service = get_service(db)
    return service.get_todo(todo_id)


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: UUID,
    todo: TodoUpdate,
    db: Session = Depends(get_db)
):
    service = get_service(db)

    existing = service.get_todo(todo_id)

    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(existing, key, value)

    return service.update_todo(existing)


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: UUID,
    db: Session = Depends(get_db)
):
    service = get_service(db)
    service.delete_todo(todo_id)

    return {
        "message": "Todo deleted successfully."
    }