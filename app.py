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
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

