import fitz  # PyMuPDF
import os
import re

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"❌ Failed to parse {pdf_path}: {e}")
        return None

def parse_cv(cv_text: str) -> dict:
    lines = cv_text.split('\n') if cv_text else []
    data = {
        "name": None,
        "phone": None,
        "email": None,
        "skills": [],
        "experience": [],
        "certifications": [],
        "achievements": []
    }

    # Basic Regex Rules
    phone_regex = re.compile(r'\+?\d[\d\s\-\(\)]{8,}')
    email_regex = re.compile(r'[\w\.-]+@[\w\.-]+')

    for line in lines:
        if not data["name"] and line.strip():
            data["name"] = line.strip()

        if not data["phone"]:
            phone_match = phone_regex.search(line)
            if phone_match:
                data["phone"] = phone_match.group()

        if not data["email"]:
            email_match = email_regex.search(line)
            if email_match:
                data["email"] = email_match.group()

        if 'skill' in line.lower():
            data["skills"].append(line.strip())
        if 'experience' in line.lower():
            data["experience"].append(line.strip())
        if 'certification' in line.lower():
            data["certifications"].append(line.strip())
        if 'achievement' in line.lower():
            data["achievements"].append(line.strip())

    return data

def parse_all_cvs(folder_path: str) -> list:
    results = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            try:
                text = extract_text_from_pdf(path)
                if not text:
                    print(f"⚠️ Skipping unreadable or empty file: {file}")
                    continue
                parsed = parse_cv(text)
                parsed["file_name"] = file
                results.append(parsed)
            except Exception as e:
                print(f"❌ Error parsing {file}: {e}")
                continue
    return results

