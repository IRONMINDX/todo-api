from re import search

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
    
    def get_all_todos(self,
                      page:int=1,page_size:int=10,search:str=None,status:str=None,priority:str=None):
        query = self.db.query(Todo)
        if search:
            query = query.filter(Todo.title.ilike(f"%{search}%"))
        if status:
            query = query.filter(Todo.status == status)
        if priority:
            query = query.filter(Todo.priority == priority)
        offset = (page - 1) * page_size
        return query.offset(offset).limit(page_size).all()        
        

    def update_todo(self, todo: Todo):
        self.db.commit()
        return todo

    def delete_todo(self, todo: Todo):
        self.db.delete(todo)
        self.db.commit()

    