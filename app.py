@app.route("/generate-title", methods=["POST"])
def generate_title():
    try:
        data = request.get_json()
        video_description = data.get("description")

        if not video_description:
            return jsonify({"error": "Description is required"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert YouTube title generator. Always create catchy, relevant, and viral titles."},
                {"role": "user", "content": f"Generate a viral, click-worthy YouTube video title for this video description: {video_description}"}
            ],
            max_tokens=50,
            temperature=0.7,
        )

        title = response["choices"][0]["message"]["content"].strip()
        return jsonify({"title": title})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
