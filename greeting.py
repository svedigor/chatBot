from datetime import datetime
import random

greetings = ("hello", "hi", "what's up", "good morning", "good evening", "good afternoon", "how are you")
boto_response = {
    "morning": ["good morning", "morning"],
    "afternoon": ["good afternoon","hey", "hi", "hello", "it's nice to see you", ],
    "evening": ["good evening"],
    "regular": ["hello", "hi"],
}
greet = "how are you"
curentTime = datetime.now()
morning = range(4,11)
afternoon = range(11,18)
evening = range(18,24)
def greet_user(sentence):
    new_str = sentence.split()
    for word in new_str:
        word = word.lower()
        if word in greetings and curentTime.hour in morning:
            return random.choice(boto_response["morning"]),greet
        elif word in greetings and curentTime.hour in afternoon:
            return random.choice(boto_response["afternoon"]),greet
        elif word in greetings and curentTime.hour in evening:
            return boto_response["evening"], greet
        else:
            return random.choice(boto_response["regular"]),greet
