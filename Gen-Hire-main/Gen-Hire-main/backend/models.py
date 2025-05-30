# backend/models.py
from sqlalchemy import Column, Integer, String, Float
from backend.db import Base

class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    job_title = Column(String)
    match_score = Column(Float)
