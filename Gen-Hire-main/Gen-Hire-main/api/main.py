from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import create_table
from api.routes import match
from routes.match import match_router
app = FastAPI(
    title="Multi-Agent Job Matcher API",
    version="1.0.0"
)
create_table()  # ✅ Create table when app starts
# Enable CORS for frontend requests (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers

app.include_router(match.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Multi-Agent Job Matcher API!"}