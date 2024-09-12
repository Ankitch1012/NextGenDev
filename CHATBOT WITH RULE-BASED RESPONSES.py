import random
import datetime

def chatbot():
    print("Hello, I'm ChatBot. How can I assist you today?")

    while True:
        user_input = input("You: ").lower()

        # Greetings based on time
        if "hello" in user_input or "hi" in user_input:
            current_hour = datetime.datetime.now().hour
            if current_hour < 12:
                print("ChatBot: Good morning! How can I assist you today?")
            elif 12 <= current_hour < 18:
                print("ChatBot: Good afternoon! What can I do for you?")
            else:
                print("ChatBot: Good evening! What can I do for you?")
        
        # Help response
        elif "help" in user_input:
            print("ChatBot: I'm here to help. Please tell me more specifically how you need assistance.")
        
        # Handling thank you
        elif "thank you" in user_input or "thanks" in user_input:
            print("ChatBot: You're very welcome! Anything else I can help with?")
        
        # Jokes
        elif "joke" in user_input:
            jokes = ["Why don't scientists trust atoms? Because they make up everything!",
                     "How do you organize a space party? You planet.",
                     "Why did the scarecrow win an award? Because he was outstanding in his field."]
            print("ChatBot:", random.choice(jokes))

        # Motivational quotes
        elif "quote" in user_input or "motivate" in user_input:
            quotes = ["Believe you can and you're halfway there. —Theodore Roosevelt",
                      "It does not matter how slowly you go as long as you do not stop. —Confucius",
                      "You are never too old to set another goal or to dream a new dream. —C.S. Lewis"]
            print("ChatBot:", random.choice(quotes))
        
        # Goodbye
        elif "bye" in user_input:
            print("ChatBot: Goodbye! Have a great day!")
            break
        
        # Unknown input
        else:
            print("ChatBot: I'm not sure how to respond to that. Can you try asking something else or use keywords like 'help', 'joke', or 'quote'?")

if __name__ == "__main__":
    chatbot()
