from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import smtplib
from email.message import EmailMessage
import os

router = APIRouter()

# Setup env vars or config
SENDER_EMAIL = os.getenv("SENDER_EMAIL") or "your.email@example.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") or "your-email-password"  # Use env vars in production

class MailRequest(BaseModel):
    name: str
    email: str
    match_score: float
    job_title: str

@router.post("/send_interview_mail")
async def send_mail(req: MailRequest):
    msg = EmailMessage()
    msg["Subject"] = f"Interview Opportunity for {req.job_title}"
    msg["From"] = SENDER_EMAIL
    msg["To"] = req.email

    msg.set_content(f"""
    Dear {req.name},

    Congratulations! You have been shortlisted for the position of {req.job_title} with a match score of {req.match_score}%.

    We would love to schedule an interview with you. Please reply to this email with your availability.

    Best regards,
    Talent Acquisition Team
    """)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/test")
def test_mail():
    return {"message": "Interview mail route working!"}