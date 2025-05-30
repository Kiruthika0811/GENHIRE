# backend/test_match.py

from backend.agents.jd_analyzer import extract_sections
from backend.agents.cv_parser import parse_all_cvs
from backend.agents.matcher import get_match_score

# Load a sample JD (manually or from CSV)
sample_jd = """
Description:
We are seeking an innovative and strategic Product Manager to lead the development and execution of new products. The ideal candidate will collaborate with cross-functional teams to define product roadmaps, analyze market trends, and ensure successful product launches.

Responsibilities:

Define product vision and strategy based on market research and customer needs.
Work closely with engineering, design, and marketing teams to develop and launch products.
Prioritize features, create roadmaps, and manage product lifecycle.
Analyze user feedback and data to optimize product performance.
Ensure alignment between business goals and product development.
Qualifications:

Bachelor's degree in Business, Computer Science, or a related field.
Experience in product management, agile methodologies, and market research.
Strong analytical, leadership, and communication skills.
Familiarity with project management tools and data-driven decision-making.
"""

jd = extract_sections(sample_jd)
cvs = parse_all_cvs("data/CVs1")  # Adjust path as needed

for cv in cvs:
    result = get_match_score(jd, cv)
    print(f"{result['candidate_name']} => Match: {result['match_score']}%")
