# backend/api/routes/match.py

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from agents.jd_analyzer import analyze_job_description
from agents.cv_parser import parse_all_cvs
from agents.matcher import match_jd_and_cvs

CV_FOLDER = "data/CVs1"
JD_CSV_PATH = "data/job_description.csv"

router = APIRouter(prefix="/match", tags=["match"])

@router.post("/run-matcher")
def run_matcher(job_title: dict):
    try:
        title = job_title.get("job_title")
        print(f"🔍 Running matcher for: {title}")

        # Get analyzed job description
        jd_result = analyze_job_description(JD_CSV_PATH, title)
        if "error" in jd_result:
            return JSONResponse(status_code=404, content=jd_result)

        # Parse all CVs
        parsed_cvs = parse_all_cvs(CV_FOLDER)
        if not parsed_cvs:
            return JSONResponse(status_code=200, content={"error": "No valid CVs found. Please check the files."})

        # Match and return ranked list
        match_result = match_jd_and_cvs(jd_result["combined_text"], parsed_cvs)
        return {"shortlisted": match_result}

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
