# backend/agents/matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_jd_and_cvs(job_keywords: str, parsed_cvs: list) -> list:
    scored = []

    for cv in parsed_cvs:
        cv_text = f"{cv.get('name', '')}\n{cv.get('skills', [])}\n{cv.get('experience', [])}\n{cv.get('certifications', [])}\n{cv.get('achievements', [])}"
        documents = [job_keywords, cv_text]

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

        scored.append({
            "user_id": parsed_cvs.index(cv) + 1,
            "name": cv.get("name"),
            "email": cv.get("email"),
            "phone": cv.get("phone"),
            "accuracy": round(similarity * 100, 2)  # percentage
        })

    # Sort by accuracy in descending order
    return sorted(scored, key=lambda x: x["accuracy"], reverse=True)
