from EmotionDetection import emotion_detector

def test_emotion(text, right_emotion):
    result = emotion_detector(text)
    dominant = result['dominant_emotion']
    if dominant == right_emotion:
        print(f"pass: '{text}' dominant emotion: {dominant}")
    else:
        print(f"fail: '{text}' expected: {right_emotion}, got: {dominant}")

test_emotion("I am glad this happened", "joy")
test_emotion("I am really mad about this", "anger")
test_emotion("I feel disgusted just hearing about this", "disgust")
test_emotion("I am so sad about this", "sadness")
test_emotion("I am really afraid that this will happen", "fear")