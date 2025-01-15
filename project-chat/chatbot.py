import random
import json

#Load responses from JSON file

def load_responses(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

#Generate a random agent name in the chat

def random_agent_name():
    agent_names = ["Mike", "Jordan", "Taylor", "Abel", "Ronaldo", "Mikasa", "Saira", "catryn"]
    return random.choice(agent_names)

#Chatbot main function

def chatbot():
    data = load_responses("responses.json")
    keywords = data["keywords"]
    generic_responses = data["generic_responses"] 
    exit_phrases = data["exit_phrases"]

#Greeting when chatbot Run

    print("Welcome to the University of Poppleton\n ")
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! You are now chatting with {random_agent_name()}.")

#Log file for the session

    log_file = f"{user_name}_chat_log.txt"
    with open(log_file, "w") as log:
        log.write(f"Chat session with {user_name}\n\n")

    while True:
        user_input = input(f"{user_name}: ").strip().lower()

#Log the user input

        with open(log_file, "a") as log:
            log.write(f"User: {user_input}\n")

#Exit conditions

        if user_input in exit_phrases:
            print(f"Goodbye, {user_name}! Have a great day!")
            with open(log_file, "a") as log:
                log.write("Session ended by user.\n")
            break

#Random disconnection (1 in 20 chance)

        if random.randint(1, 20) == 1:
            print("Oops! The chat system has disconnected. Please try again later.")
            with open(log_file, "a") as log:
                log.write("Session ended due to random disconnection.\n")
            break

#Keyword detection

        response = None
        for keyword, reply in keywords.items():
            if keyword in user_input:
                response = reply
                break

#Respond to user

        if response:
            response = response.replace("{user_name}", user_name)
            print(response)
            with open(log_file, "a") as log:
                log.write(f"Agent: {response}\n")
        else:
            random_response = random.choice(generic_responses)
            random_response = random_response.replace("{user_name}", user_name)
            print(random_response)
            with open(log_file, "a") as log:
                log.write(f"Agent: {random_response}\n")

#Run the chatbot

if __name__ == "__main__":
    chatbot()
