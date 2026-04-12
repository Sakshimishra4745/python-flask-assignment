def emotion_detector(text_to_analyze):
    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.1,
        "joy": 0.6,
        "sadness": 0.15
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return f"""
For the given statement, the system response is:
anger: {emotions['anger']}, disgust: {emotions['disgust']}, fear: {emotions['fear']}, joy: {emotions['joy']}, sadness: {emotions['sadness']}.
The dominant emotion is {dominant_emotion}.
"""