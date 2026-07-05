from app.models import user
from app.repositories.user_repository import UserRepository
from app.models.user import User

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user:User):
        if not user.full_name.strip():
            raise ValueError("Full name cannot be empty.")
        
        if "@" not in user.email or "." not in user.email:
            raise ValueError("Invalid email format.")
    
        existing_user=self.repository.get_user_by_email(user.email)
        if existing_user:
             raise ValueError("Email already exists.")
        self.repository.create_user(user)

        return self.repository.create_user(user)