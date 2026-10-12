from flask import Flask, jsonify, request
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)


@app.route("/api/assess", methods=["POST"])
def assess():
  data = request.json
  answers = data.get("answers", [])

  prompt = (
      "You are Defshield, a mental health screening assistant. Analyze these"
      f" 15 survey answers and write an empathetic report with a medical disclaimer:\n"
      + "\n".join([f"Q{i+1}: {a}" for i, a in enumerate(answers)])
  )

  res = ollama.chat(
      model="gemma:2b",
      messages=[{"role": "user", "content": prompt}],
  )
  return jsonify({"report": res["message"]["content"]})


if __name__ == "__main__":
  app.run(port=5000)
