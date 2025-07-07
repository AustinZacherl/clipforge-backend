from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI key here or use environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/title", methods=["POST"])
def generate_title():
    data = request.json
    transcript = data.get("transcript", "")

    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": f"Write a viral YouTube video title based on this: {transcript}"}
        ]
    )

    return jsonify({"title": response.choices[0].message.content.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
