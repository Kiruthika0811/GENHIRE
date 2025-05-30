from fastapi import APIRouter, Body
from agents.jd_analyzer import extract_sections
import pandas as pd
import os

router = APIRouter()

@router.get("/all")
def get_all_job_descriptions():
    try:
        df = pd.read_csv(JD_FILE_PATH)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@router.get("/{job_title}")
def get_job_description_by_title(job_title: str):
    try:
        df = pd.read_csv(JD_FILE_PATH)
        match = df[df["job_title"].str.lower() == job_title.lower()]
        if not match.empty:
            return match.to_dict(orient="records")[0]
        return {"message": "Job title not found"}
    except Exception as e:
        return {"error": str(e)}