import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Charles Dickens"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Gold", "Silver", "Iron"],
        "answer": "Oxygen"
    }
]

# Global variables
current_question = 0
score = 0

# Function to load the next question
def load_question():
    global current_question
    if current_question < len(questions):
        question_data = questions[current_question]
        question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            option_buttons[i].config(text=option, state=tk.NORMAL)
    else:
        messagebox.showinfo("Quiz Over", f"Your final score is {score}/{len(questions)}")
        root.destroy()

# Function to check the answer
def check_answer(selected_option):
    global current_question, score
    question_data = questions[current_question]
    if question_data["options"][selected_option] == question_data["answer"]:
        score += 1
        messagebox.showinfo("Correct", "Your answer is correct!")
    else:
        messagebox.showinfo("Incorrect", f"Wrong answer! The correct answer is {question_data['answer']}.")
    current_question += 1
    score_label.config(text=f"Score: {score}/{len(questions)}")
    load_question()

# Create the main window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("500x400")

# Question label
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450)
question_label.pack(pady=20)

# Option buttons
option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=("Arial", 12), width=20,
                       command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    option_buttons.append(button)

# Score label
score_label = tk.Label(root, text="Score: 0/0", font=("Arial", 12))
score_label.pack(pady=10)

# Load the first question
load_question()

# Run the application
root.mainloop()