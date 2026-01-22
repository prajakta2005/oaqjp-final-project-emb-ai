"""
Flask server for Emotion Detection application.

This module provides web endpoints to analyze emotions
from user-provided text using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the home page.

    Returns:
        HTML template for the main interface.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyze emotions from the provided text input.

    Returns:
        A formatted string containing emotion scores and
        the dominant emotion, or an error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
