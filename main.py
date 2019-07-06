from greeting import greet_user
from jokes import get_joke
from weather import get_weather

def main_chat(user_input):
    greetings = ("hello", "hi", "what's up", "good morning", "good evening", "good afternoon", "how are you")
    answer = user_input.split()
    for word in answer:
        if word in greetings:
            return greet_user(word)
        elif word == "joke":
            return get_joke()
        else:
            return get_weather(user_input)

