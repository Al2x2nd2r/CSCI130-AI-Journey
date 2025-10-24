# hello_ai.py
# Alexander Lupear
# CSCI 130 - Week 1 Project
# Date: [10/24/2025]
import random
import datetime

def greeting_agent():
    # A simple AI agent that provides personalized greetings
    # This demonstrates a simple reflex agent from chapter 2

    print("Script Started")
    
    # Get current time
    current_hour = datetime.datetime.now().hour
    
    # Determine time of day

    if current_hour < 12:
        time_period = "morning"
    elif current_hour < 17:
        time_period = "afternoon"
    else:
        time_period = "evening"

    # Get user's name
    name = input("What's your name?")

    # Generates personalized greeting
    greetings = [
        f"Good {time_period}, {name}! Welcome to AI class!",
        f"Hello {name}! Hope you're having a great {time_period}!",
        f"Hi {name}! Ready to learn AI this {time_period}?"
    ]

    # Select and display random greeting
    print(random.choice(greetings))

    # Simple conversation
    mood = input("\nHow are you feeling about learning AI? ")

    # Simple response based on keywords (Reflex-Agent Behavior)
    if "excited" in mood.lower() or "good" in mood.lower():
        print ("That's wonderful! Your enthusiasm will help you learn!")
    elif "nervous" in mood.lower() or "worried" in mood.lower():
        print ("Don't worry! We'll take it step by step.")
    elif "anxious" in mood.lower() or "scared" in mood.lower():
        print ("Don't worry! We'll take it nice and slow!")    
    else:
        print(f"Thanks for sharing! Let's make this a great learning expirience!")

    # Display an AI fact
    ai_facts = [
        "Did you know? The term 'Artificial Intelligence' was coined in 1956!",
        "Fun fact: Your smartphone uses AI for face recognition!",
        "AI insight: Netflix uses AI to recommend shows you might like!",
        "Did you know? AI helps doctors detect diseases earlier!",
        "Some AI systems, like Google’s Magenta, can compose original songs in different genres",
        "DeepMind’s AlphaGo became the first AI to defeat a human world champion in the complex board game Go, which has more possible moves than atoms in the universe."
    ]

    print(f"n\{random.choice(ai_facts)}")
    print ("\n Let's start out AI journey together!")

    # Run the program
if __name__ == "__main__":
        print("=" * 50)
        print("Welcome to CSCI 130: Introduction to AI")
        print("=" * 50)
        print()
        greeting_agent()