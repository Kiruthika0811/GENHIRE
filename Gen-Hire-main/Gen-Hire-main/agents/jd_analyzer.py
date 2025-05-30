# backend/agents/jd_analyzer.py

import pandas as pd

def analyze_job_description(csv_path: str, job_title: str) -> dict:
    df = pd.read_csv(csv_path)

    job_row = df[df["Job Title"].str.lower() == job_title.lower()]

    if job_row.empty:
        return {"error": f"No job description found for title: {job_title}"}

    job_row = job_row.iloc[0]

    description = str(job_row.get("Description", ""))
    responsibilities = str(job_row.get("Responsibilities", ""))
    qualifications = str(job_row.get("Qualifications", ""))

    # Combine all into a single chunk of relevant text
    job_keywords = f"{description}\n{responsibilities}\n{qualifications}"

    return {
        "job_title": job_title,
        "description": description,
        "responsibilities": responsibilities,
        "qualifications": qualifications,
        "combined_text": job_keywords
    }
