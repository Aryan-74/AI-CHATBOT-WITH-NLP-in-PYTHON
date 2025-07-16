# AI-CHATBOT-WITH-NLP-in-PYTHON

this is the third project of my first summer internship in python programming

COMPANY: CODTECH IT SOLUTIONS

NAME: Aryan Jain

INTERN ID: CT04DG1236

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

DESCRIPTION:

**Overview:**

Task 3 of the CODTECH Python internship challenges students to build a functional chatbot using Natural Language Processing (NLP) libraries such as **NLTK** (Natural Language Toolkit) or **spaCy**. This task is an introduction to the fascinating world of AI-powered conversational agents. Chatbots have become a key feature in modern applications, from customer service to productivity tools, and building one helps interns gain practical experience in how machines can process and respond to human language.



**Objective:**

The primary objective of this task is to develop a **rule-based chatbot** that can understand basic user inputs and provide appropriate responses. The chatbot should be capable of:

* Recognizing greetings and common phrases
* Responding to queries related to the internship or task guidance
* Handling unmatched input gracefully
* Providing a smooth, interactive experience on the command line

This task introduces key NLP concepts such as pattern matching, tokenization, and simple intent recognition. The goal is not to create a perfect AI assistant but to understand the fundamentals of language-based interaction in Python.



**Approach:**

To implement the chatbot, the **NLTK** library was used due to its simplicity and excellent support for text processing tasks. Specifically, NLTK’s `Chat` class and `reflections` dictionary were used to build a rule-based conversational bot.

The core of the chatbot is built around **“pairs”** — a list of regular expression patterns mapped to potential responses. For example, if a user says "Hi", the bot matches it to the greeting pattern and responds with "Hello there!" or similar options.

These pairs were defined to handle:

* Greetings ("hi", "hello")
* Questions about the bot itself ("what is your name?")
* Queries related to internship tasks ("what is task 1?")
* Generic help questions ("how do I install a package?")
* Exit commands ("quit", "bye")

Using NLTK’s `Chat` class, a chatbot object was created using these pairs and the built-in `reflections`, which helps convert "I am" to "you are", making the conversation feel more natural.

The chatbot runs in the terminal, continuously asking for user input and responding appropriately. It exits cleanly when the user types a farewell keyword like "quit".



**Enhancements and Features:**

To make the chatbot more interactive and intelligent, additional improvements were made:

* Added multiple patterns for each intent using regular expressions (e.g., recognizing both "how are you?" and "how r u?")
* Extended the pairs list to include all four internship task descriptions
* Implemented a fallback response for unmatched input ("I'm not sure I understand. Can you rephrase?")
* Provided responses based on task numbers, guiding the user with task-specific explanations

These enhancements made the chatbot a more useful assistant during the internship itself — serving as a quick reference guide for the tasks.



**Learning Outcomes:**

This task helped develop key skills in:

* **Natural Language Processing (NLP)** fundamentals using Python
* Writing and using **regular expressions** for intent detection
* Structuring a rule-based chatbot using **NLTK’s Chat class**
* Understanding the limitations of pattern-based AI and the foundation it provides for building smarter bots
* Improving user interaction with dynamic, console-based conversations

It also encouraged interns to think about how real-world chatbots are built, and how rule-based bots differ from machine learning or neural network-based chatbots like ChatGPT or Alexa.



**Conclusion:**

Task 3 was both educational and enjoyable, giving interns a chance to step into the world of AI with hands-on experience. Although the chatbot was simple and rule-based, it served as an effective entry point into conversational interfaces and natural language understanding. By completing this task, interns gained confidence in using Python for text processing, learned how to create basic conversational logic, and understood how real-world bots are structured and built. It also prepared them for more advanced chatbot development using intent classification, dialogue management, and integration with APIs or UI frameworks.

OUTPUT : <img width="1466" height="447" alt="output-terminal" src="https://github.com/user-attachments/assets/52fbbb4e-7c7c-4370-8a2a-41b49a6cd279" />
