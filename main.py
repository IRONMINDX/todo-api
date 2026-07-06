from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.todo import router as todo_router
import app.models

app= FastAPI(
    title="todo api",
    version="1.0.0",
)
app.include_router(todo_router)
app.include_router(health_router)