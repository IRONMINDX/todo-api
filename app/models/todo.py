import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
from sqlalchemy .orm import relationship

class Todo(Base):
    __tablename__ = "todos"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id= Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="todos")

