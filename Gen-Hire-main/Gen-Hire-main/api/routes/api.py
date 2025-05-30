# backend/routes/api.py
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

class MatchResult(BaseModel):
    job_title: str
    candidate_name: str
    match_score: float

@router.get("/")
def read_root():
    return {"message": "Welcome to Job Matcher AI"}

@router.get("/matches", response_model=List[MatchResult])
def get_matches():
    # In future, pull from matcher module or DB
    return [
        MatchResult(job_title="Software Engineer", candidate_name="John Doe", match_score=87.5),
        MatchResult(job_title="Data Scientist", candidate_name="Jane Smith", match_score=82.3)
    ]
from fastapi import APIRouter
from .cv import router as cv_router
from .jd import router as jd_router
from .match import router as match_router
from .interview_mail import router as mail_router

router = APIRouter()

# Mount each router to its own path prefix
router.include_router(cv_router, prefix="/cv", tags=["CV"])
router.include_router(jd_router, prefix="/jd", tags=["JD"])
router.include_router(match_router, prefix="/match", tags=["Match"])
router.include_router(mail_router, prefix="/mail", tags=["Interview Mail"])
