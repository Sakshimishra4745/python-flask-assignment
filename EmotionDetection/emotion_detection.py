def emotion_detector(text_to_analyze):
    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.1,
        "joy": 0.6,
        "sadness": 0.15
    }

    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        "emotion": emotions,
        "dominant_emotion": dominant_emotion
    }

    return result

print(emotion_detector("I am happy"))