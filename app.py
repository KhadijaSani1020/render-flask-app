from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route('/')
def home():
    return "Hello World from Render + PostgreSQL!"

@app.route('/create')
def create_table():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, name TEXT);")
        conn.commit()
        cur.close()
        conn.close()
        return "Table created successfully!"
    except Exception as e:
        return f"Error: {e}"
