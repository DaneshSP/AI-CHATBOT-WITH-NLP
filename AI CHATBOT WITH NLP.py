import nltk
from nltk.chat.util import Chat, reflections

# Download punkt tokenizer if not already installed
nltk.download('punkt')

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Greetings! How can I help you?"]],
    [r"how are you ?", ["I'm doing well, thank you!", "I'm a bot, but I'm functioning as expected! And you?"]],
    [r"what is your name ?", ["I'm a chatbot built with NLP using NLTK.", "You can call me NLP Bot!"]],
    [r"(.*) your name ?", ["My name is NLP Bot!", "I'm called NLP Bot."]],
    [r"who created you ?", ["I was created by a developer who loves NLP."]],
    [r"what can you do ?", ["I can chat with you, answer simple questions, and help you learn NLP concepts!"]],
    [r"(.) help (.)", ["Sure, how can I assist you?", "I'm here to help! What do you need?"]],
    [r"(quit|bye|exit)", ["Bye! Have a great day!", "Goodbye!"]],
    [r"(.*)", ["I'm sorry, I don't understand that yet. Can you rephrase?"]]
]

def chatbot():
    print("NLP Chatbot\nType 'quit', 'bye', or 'exit' to leave.")
    chat = Chat(pairs, reflections)
    chat.converse()
    
if __name__ == "__main__":
    chatbot()