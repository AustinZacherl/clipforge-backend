from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load GPT-2 model pipeline once at startup (takes a few seconds)
generator = pipeline('text-generation', model='gpt2')

@app.route("/generate-title", methods=["POST"])
def generate_title():
    try:
        data = request.get_json()
        video_description = data.get("description")

        if not video_description:
            return jsonify({"error": "Description is required"}), 400

        prompt = f"Generate a catchy YouTube video title for: {video_description}"
        results = generator(prompt, max_length=30, num_return_sequences=1)
        title = results[0]['generated_text']

        # Clean up the title text a bit (remove prompt from generated text)
        title = title.replace(prompt, '').strip()
        return jsonify({"title": title})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
