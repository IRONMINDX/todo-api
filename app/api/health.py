from fastapi import APIRouter

app = APIRouter()

@app.get("/health")
def health():
    return {"status": "healthy"}
