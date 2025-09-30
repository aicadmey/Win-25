from textblob import TextBlob

# Emotion-based responses
responses = {
    "happy": "I'm glad you're happy! Keep smiling 😊",
    "sad": "I'm sorry to hear that. Remember, I'm here to support you. ❤️",
    "angry": "It’s okay to feel angry sometimes. Take a deep breath, and let’s talk it out. 🌬️",
    "anxious": "I understand you're feeling anxious. Try to focus on your breath and relax. 🧘",
    "lonely": "You are not alone! I'm here to keep you company. 🤗",
    "bored": "Let’s find something fun to do! What do you enjoy the most? 🎲",
    "confused": "I'm here to help! Can you tell me more about what's confusing you? 🤔",
    "hopeful": "It’s wonderful to feel hopeful. Keep believing in yourself! 🌟",
    "neutral": "Tell me more about your day. I’d love to hear! 😊"
}

# Small talk responses
small_talk = {
    "hello": "Hello! I'm Raymax, your personal emotional support bot. How can I help you today? 🤖",
    "thank you": "You're welcome! I'm always here to help. 😊",
    "what's your name?": "I’m Raymax, your friendly emotional support robot. 🤖",
    "bye": "Take care! I’m always here if you need me. Goodbye! 👋",
    "exit": "Take care! I’m always here if you need me. Goodbye! 👋"
}

# Function to detect emotion using simple sentiment analysis
def detect_emotion(user_input):
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    if sentiment > 0.5:
        return "happy"
    elif sentiment > 0:
        return "hopeful"
    elif sentiment < -0.5:
        return "angry"
    elif sentiment < 0:
        return "sad"
    elif "bored" in user_input.lower():
        return "bored"
    elif "anxious" in user_input.lower() or "nervous" in user_input.lower():
        return "anxious"
    elif "lonely" in user_input.lower():
        return "lonely"
    elif "confused" in user_input.lower():
        return "confused"
    else:
        return "neutral"

# Function to handle small talk
def respond_to_small_talk(user_input):
    for key in small_talk:
        if key in user_input.lower():
            return small_talk[key]
    return None

# Raymax main program
def raymax():
    print("Raymax: Hi! I’m Raymax, your personal emotional support bot. How are you feeling today? (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")  
        
        # Check for exit keywords
        if user_input.lower() in ["bye", "exit"]:
            print(f"Raymax: {small_talk['bye']}")
            break

        # Handle small talk
        response = respond_to_small_talk(user_input)
        if response:
            print(f"Raymax: {response}")
        else:
            # Detect emotion and respond accordingly
            emotion = detect_emotion(user_input)
            print(f"Raymax: {responses.get(emotion, 'I’m here to listen. Tell me more.')}")
            

raymax()
 


#  This program will further integrated into main raymax program after further more improvements