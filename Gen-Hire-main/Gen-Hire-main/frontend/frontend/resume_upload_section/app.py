from flask import Flask, render_template, request, redirect, url_for
import os
import spacy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def evaluate_resume(text):
    skills = ['Python', 'SQL', 'Machine Learning', 'Data Visualization', 'NLP']
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    score = int((len(found_skills) / len(skills)) * 100)
    return found_skills, score

@app.route('/')
def index():
    return render_template('page1.html')  # This is your upload page

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()

        found_skills, score = evaluate_resume(text)
        result = "Shortlisted ✅" if score >= 50 else "Not Shortlisted ❌"

        return render_template('result.html', skills=found_skills, score=score, result=result)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

