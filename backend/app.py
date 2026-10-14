from flask import Flask, jsonify, request
from database import init_db, get_db

app = Flask(__name__)

questions = [
    {"id": 1, "text": "Tell me about yourself."},
    {"id": 2, "text": "Walk me through your Python experience."},
    {"id": 3, "text": "What about React? How much have you worked with it?"},
    {"id": 4, "text": "How does React work with a Python backend?"},
    {"id": 5, "text": "What's the most challenging thing you've worked on?"},
    {"id": 6, "text": "Why are you looking for a new role?"},
]

@app.get("/api/questions")
def get_questions():
    return jsonify(questions)

@app.get("/api/answers")
def get_answers():
    conn = get_db()
    rows = conn.execute("SELECT * FROM answers").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.post("/api/answers")
def add_answer():
    data = request.get_json(silent=True) or {}
    question_id = data.get("question_id")
    text = (data.get("text") or "").strip()

    if not any(q["id"] == question_id for q in questions):
        return jsonify("error: unknown question id"), 400
    if not text:
        return jsonify("error: answer text is required"), 400

    conn = get_db()
    cur = conn.execute("INSERT INTO answers (question_id, text) VALUES (?, ?)", (question_id, text))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()

    answer = {
        "id": new_id,
        "question_id": question_id,
        "text": text,
    }

    return jsonify(answer), 201






if __name__ == "__main__":
    init_db()
    app.run(port=5001, debug=True)