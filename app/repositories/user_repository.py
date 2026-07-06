from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update_user(self, user: User):
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete_user(self, user: User):
        self.db.delete(user)
        self.db.commit()

    def get_user(self,user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self,email):
        return self.db.query(User).filter(User.email == email).first()