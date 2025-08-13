from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Please enter text to analyze.", 400
    response = emotion_detector(text_to_analyze)
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)