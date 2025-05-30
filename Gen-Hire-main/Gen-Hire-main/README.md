# 🤖 AI-Powered Job Matching System

A smart recruitment assistant that matches job descriptions with candidate CVs using NLP and AI. Designed to streamline hiring by automating shortlisting based on skills, experience, and job fit.

---

## 🗂 Project Structure

gen_hiring/ │ ├── backend/ │ ├── agents/ # Core logic modules │ │ ├── jd_analyzer.py # Parses and extracts JD sections │ │ ├── matcher.py # Matches JD and CVs based on embeddings │ │ └── cv_parser.py # Extracts structured data from CVs │ │ │ ├── api/ │ │ ├── routes/ │ │ │ └── match.py # FastAPI route for matching │ │ └── main.py # FastAPI app entry point │ │ │ ├── database/ │ │ └── db.py # SQLite database (optional future feature) │ ├── data/ │ ├── CVs1/ # Folder containing CV PDFs │ └── job_description.csv # CSV file with job descriptions │ ├── README.md # This file └── requirements.txt # Python dependencies


---

## 🚀 Features

- 🔍 **JD Analyzer:** Extracts and combines job role descriptions, responsibilities, and qualifications.
- 📄 **CV Parser:** Parses CVs from PDF and extracts text.
- 🤝 **AI Matcher:** Uses NLP embeddings to rank candidates based on JD relevance.
- 📦 **FastAPI Backend:** Clean and modular API design.

---

## 🧪 Sample Request

### POST `/match/run-matcher`

```json
{
  "job_title": "Data Analyst"
}
Response:
{
  "shortlisted": [
    {
      "name": "Alice Smith",
      "match_score": 0.91,
      "skills": "Python, SQL, Tableau",
      "experience": "2+ years in analytics"
    },
    ...
  ]
}
⚙️ How to Run Locally
1. Clone the repo

git clone https://github.com/your-username/gen_hiring.git
cd gen_hiring/backend
2. Set up a virtual environment

python -m venv venv
source venv/Scripts/activate   # On Windows
3. Install dependencies

pip install -r requirements.txt
4. Run FastAPI server

uvicorn api.main:app --reload

Visit: http://127.0.0.1:8000/docs for the Swagger UI.

📄 Data Format
job_description.csv
job_title	description	responsibilities	qualifications
Data Analyst	Analyze and visualize data...	Collect, clean, visualize...	BSc in CS, 2+ yrs exp...
...	...	...	...

Tech Stack
Language: Python 3.11

Framework: FastAPI

Parsing: PyMuPDF (fitz)

NLP: sentence-transformers (all-MiniLM-L6-v2)

Database (optional): SQLite

 Todo / Future Scope
 Add UI (React)

 Include candidate feedback + rating system

 Interview scheduler agent

 Handle large-scale job and CV datasets

 Email notifications for shortlisted candidates

Credits
Developed by Jenilia Gracelyn
B.E. CSE - AIML | SRM Easwari Engineering College

Developed by Kiruthika.B
B.Tech IT | SRM Easwari Engineering College

 License
This project is licensed under the MIT License. Feel free to use and extend it!