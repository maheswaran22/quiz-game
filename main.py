from random import random

import mport as mport

#mport random

# Load quiz questions and answers from a file or a database
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": 0
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Jupiter", "Saturn", "Mars", "Earth"],
        "correct_answer": 0
    },
    # Add more questions as needed
]

# Calculate the final score
def calculate_score(questions, user_answers):
    score = 0
    for i, question in enumerate(questions):
        if user_answers[i] == question["correct_answer"]:
            score += 1
    return score

# Display a welcome message and rules
print("Welcome to the Quiz Game!")
print("You will be asked a series of questions.")
print("Select the correct answer for each question.")
print("Your final score will be displayed at the end.")
# Present quiz questions
def present_questions(questions):
    user_answers = []
    for question in questions:
        print(question["question"])
        for i, answer in enumerate(question["answers"]):
            print(f"{i+1}. {answer}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        user_answers.append(user_answer)
    return user_answers

# Evaluate the user's answer
def evaluate_answers(questions, user_answers):
    score = calculate_score(questions, user_answers)
    print(f"Your final score is: {score}/{len(questions)}")

# Play again
def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        return True
    else:
        return False

# Main loop
while True:
    user_answers = present_questions(questions)
    evaluate_answers(questions, user_answers)
    if not play_again():
        break



