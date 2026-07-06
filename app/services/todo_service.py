from app.models import todo
from app.repositories import todo_repository
from app.repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository
    
    def create_todo(self, todo: todo.Todo):
        if not todo.title.strip():
            raise ValueError("Title cannot be empty.")
        
        if not todo.status.strip():
            raise ValueError("Status cannot be empty.")
        
        if not todo.priority.strip():
            raise ValueError("Priority cannot be empty.")
        
        return self.repository.create_todo(todo)
    
    def get_all_todos(self,page:int=1,page_size:int=10,search:str=None,status:str=None,priority:str=None):
        if page < 1 or page_size < 1:
            raise ValueError("Page and page size must be positive integers.")
        return self.repository.get_all_todos(page=page,page_size=page_size,search=search,status=status,priority=priority)
    
    def get_todo(self, todo_id: str):
        todo = self.repository.get_todo(todo_id)
        if not todo:
            raise ValueError("Todo not found.")
        return todo
    
    def update_todo(self, todo: todo.Todo):
        existing_todo = self.repository.get_todo(todo.id)
        if not existing_todo:
            raise ValueError("Todo not found.")
        
        if not todo.title.strip():
            raise ValueError("Title cannot be empty.")
        
        if not todo.status.strip():
            raise ValueError("Status cannot be empty.")
        
        if not todo.priority.strip():
            raise ValueError("Priority cannot be empty.")
        
        return self.repository.update_todo(todo)
    
    def delete_todo(self, todo_id: str):
        todo = self.repository.get_todo(todo_id)
        if not todo:
            raise ValueError("Todo not found.")
        self.repository.delete_todo(todo)