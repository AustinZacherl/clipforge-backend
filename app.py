from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import traceback

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/generate-title", methods=["POST"])
def generate_title():
    try:
        data = request.get_json()
        video_description = data.get("description")

        if not video_description:
            return jsonify({"error": "Description is required"}), 400

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a YouTube title generator."},
                {"role": "user", "content": f"Create a viral YouTube title for this video: {video_description}"}
            ],
            max_tokens=30,
            temperature=0.8,
        )

        title = response.choices[0].message.content.strip()
        return jsonify({"title": title})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)
