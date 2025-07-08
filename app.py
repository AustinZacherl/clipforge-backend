from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate-title', methods=['POST'])
def generate_title():
    data = request.get_json()
    input_text = data.get('input_text', '')

    # Simple example logic — you can plug in real AI later
    if not input_text:
        return jsonify({'title': 'No input provided'}), 400

    generated_title = f"Epic Clip: {input_text[:40]}..."

    return jsonify({'title': generated_title})

@app.route('/')
def home():
    return "ClipForge AI Backend is running."

