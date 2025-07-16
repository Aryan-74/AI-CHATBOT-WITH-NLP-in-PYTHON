import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs (patterns and responses)
pairs = [

    [r"hi|hello|hey", 
     ["Hello there!", "Hi! How can I help you today?", "Hey!"]],

    [r"what is your name\??", 
     ["I'm CodBot, your internship assistant."]],

    [r"how are you\??", 
     ["I'm just code, but I'm here to help you!", "Doing great, thanks!"]],

    [r"(.*) internship (.*)", 
     ["I'm here to help you complete your CodTech internship tasks.", 
      "Internship guidance is my job. Ask away!"]],

    [r"(.*) task 1 (.*)", 
     ["Task 1 involves using a public API and creating a visualization with Matplotlib or Seaborn."]],

    [r"(.*) task 2 (.*)", 
     ["Task 2 is about reading data from a file and generating a PDF report using FPDF or ReportLab."]],

    [r"(.*) task 3 (.*)", 
     ["Task 3 requires building a chatbot using NLP libraries like NLTK or spaCy. Just like me!"]],

    [r"(.*) task 4 (.*)", 
     ["Task 4 is about creating a machine learning model using scikit-learn."]],

    [r"(.*) how to (.*)", 
     ["Can you be more specific about what you want to know how to do?"]],

    [r"(.*) help (.*)", 
     ["Sure! I can help you with your internship tasks, explain Python concepts, or debug errors."]],

    [r"(.*) python (.*)", 
     ["Python is a powerful and beginner-friendly programming language. Need help with syntax or libraries?"]],

    [r"(.*) install (.*)", 
     ["You can install libraries using pip, like: pip install library_name"]],

    [r"(.*) email (.*)", 
     ["You can use smtplib in Python to send emails. I can show you a script for that."]],

    [r"(.*) quit", 
     ["Goodbye! Best of luck with your internship.", "See you later. Happy coding!"]],

    [r"(.*)", 
     ["I'm not sure I understand. Could you rephrase?", 
      "Hmm, I don't have a reply for that. Try asking about your tasks."]]
]


# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("🤖 CodTech ChatBot: Type 'quit' to exit.")
chatbot.converse()
