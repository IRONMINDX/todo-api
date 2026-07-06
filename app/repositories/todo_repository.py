from sqlalchemy.orm import Session
from app.models.todo import Todo

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_todo(self, todo: Todo):
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def get_todo(self, todo_id: str):
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def get_todos(self, user_id: str):
        return self.db.query(Todo).filter(Todo.user_id == user_id).all()
    
    def get_all_todos(self):
        return self.db.query(Todo).all()

    def update_todo(self, todo: Todo):
        self.db.commit()
        return todo

    def delete_todo(self, todo: Todo):
        self.db.delete(todo)
        self.db.commit()

    