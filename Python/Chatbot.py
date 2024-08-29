import nltk
from nltk.chat.util import Chat, reflections

# Uncomment and run this line if you haven't downloaded NLTK's 'punkt' tokenizer
# nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you today?"]
    ],

    [
        r"what is your name ?",
        ["My name is FUN Chatbot.",]
    ],

    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],

    [
        r"(what is your age ?|how old are you ?|what age are you ?|tell me your age ?)",
        ["I'm a chatbot, created by Ammar.", ]
    ],

    [
        r"(what is the code alpha website ?|do you know the code alpha website ?)",
        ["Yes, I know the Code Alpha website. Here it is: https://www.codealpha.tech/", ]
    ],

    [
        r"does code alpha offer internships ?",
        ["Yes, Code Alpha offers internships. You can check the details on their website: https://www.codealpha.tech/internship.html", ]
    ],

    [
        r"(what types of internships does code alpha offer ?|can you tell me about code alpha internships ?)",
        ["Code Alpha offers various internships, including software development, data science, and marketing. For more details, visit https://www.codealpha.tech/internship.html", ]
    ],

    [
        r"(what courses does code alpha offer ?|do you know about code alpha courses ?)",
        ["Code Alpha offers a range of courses in software development, data science, and other tech-related fields. Check their website for more information: https://www.codealpha.tech/#courses", ]
    ],

    [
        r"(where can I find code alpha's course catalog ?|how can I view code alpha's courses ?)",
        ["You can view Code Alpha's course catalog on their website at https://www.codealpha.tech/#courses", ]
    ],

    [
        r"(do you know code alpha ?|where is code alpha located ?|I want to know about code alpha|what is the location of code alpha office ?|where is the code alpha office ?)",
        ["Yes, I know Code Alpha. It's a software company located in Lucknow, India.", ]
    ],

    [
        r"sorry(.*)",
        ["No problem at all!", "It's okay!", "No worries!"]
    ],

    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "See you later!"]
    ],

    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you please rephrase?", "I'm not sure about that. Can you ask me something else?"]
    ]
]

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "me": "you",
}

def chatbot():
    print("Hi! I am a simple NLTK chatbot. Type 'bye' to exit.")

    chat = Chat(pairs, reflections)

    while True:
        user_input = input("You: ").lower()
        if user_input in ['bye', 'goodbye']:
            print("Bot: Goodbye! Have a great day!")
            break

        response = chat.respond(user_input)
        if response:
            print(f"Bot: {response}")
        else:
            print("Bot: I don't understand that.")

# Start the chatbot
chatbot()
