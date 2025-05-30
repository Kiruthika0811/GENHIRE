import sqlite3
from datetime import datetime

DB_NAME = "shortlisted.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS shortlisted_candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            match_score REAL,
            job_title TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_candidate(name, email, phone, match_score, job_title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO shortlisted_candidates (name, email, phone, match_score, job_title, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, email, phone, match_score, job_title, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_all_shortlisted():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM shortlisted_candidates')
    results = cursor.fetchall()
    conn.close()
    return results

def init_db():
    create_table()
