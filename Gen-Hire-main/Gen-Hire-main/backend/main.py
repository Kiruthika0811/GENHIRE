# backend/main.py
from fastapi import FastAPI
from backend.routes import api
import uvicorn

app = FastAPI(title="Job Matcher AI")

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
