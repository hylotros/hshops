import os
import psycopg
from flask import Flask, jsonify

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_db_connection():
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        project="HShops",
        message="Welcome to HShops",
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/version")
def version():
    return jsonify(version="1.0.0")

@app.get("/users")
def users():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, username FROM users ORDER BY id;")
            rows = cur.fetchall()

    return jsonify([
        {"id": row[0], "username": row[1]}
        for row in rows
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

