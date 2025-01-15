# Chatbot Project

This is a simple chatbot application designed to answer common questions from users. The chatbot uses predefined questions and answers stored in a JSON file to provide quick and reliable responses.

## Features

- **Predefined Responses**: The chatbot uses a JSON file to store a list of common questions and their answers.
- **Easy Customization**: You can add, update, or remove questions and answers by editing the `responses.json` file.
- **Simple Logic**: The chatbot processes user input and matches it with the predefined questions to provide an appropriate response.

## Files in the Project

1. **`chatbot.py`**

- This is the main Python file that contains the chatbot logic.
- It reads the `responses.json` file to fetch the predefined questions and answers.
- Matches user input with the stored questions to generate responses.

2. **`responses.json`**
   - A JSON file that stores a list of predefined questions and their corresponding answers.
   - Example structure:
     ```json
     {
       "What is your name?": "I am a chatbot created to assist you.",
       "How can I help you?": "You can ask me about our services, products, or general information."
     }
     ```

## How to Use

1. **Run the Chatbot**:

   - Open a terminal or command prompt.
   - Navigate to the directory containing `chatbot.py`.
   - Run the script using Python:
     ```bash
     python chatbot.py
     ```

2. **Interact with the Chatbot**:
   - Type a question that matches one in `responses.json`.
   - The chatbot will display the predefined answer.
   - If the question is not found, the chatbot will give you generic responses .

## How to Customize

1. **Add New Questions and Answers**:

   - Open `responses.json` in a text editor.
   - Add a new question and answer pair in the following format:
     ```json
     "What is the tuition fee?": "The tuition fee is $15,000 per year."
     ```
   - Ensure the file maintains proper JSON syntax.

2. **Update Existing Responses**:

- Find the question in `responses.json`.
- Modify its corresponding answer.

3. **Delete a Question**:

- Locate the question in `responses.json` and remove the question-answer pair.

## Requirements

- Python 3.x
