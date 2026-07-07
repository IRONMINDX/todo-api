from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.todo import router as todo_router
import app.models
from app.exceptions.handlers import value_error_handler, global_exception_handler
from app.middleware.logging import log_middleware

app= FastAPI(
    title="todo api",
    version="1.0.0",
)
app.add_exception_handler(ValueError, value_error_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.middleware("http")(log_middleware)


app.include_router(todo_router)
app.include_router(health_router)