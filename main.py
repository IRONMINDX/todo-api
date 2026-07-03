from fastapi import FastAPI
from app.api.health import app as health_router

app= FastAPI(
    title="todo api",
    version="1.0.0",
)
app.include_router(health_router)