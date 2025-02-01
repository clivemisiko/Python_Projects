import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables
current_player = "X"
board = [" "] * 9  # Represents the 3x3 grid
game_over = False

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            highlight_winner(combo)
            return True

    if " " not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
        return True

    return False

# Function to highlight the winning combination
def highlight_winner(combo):
    for index in combo:
        buttons[index].config(bg="light green")
    global game_over
    game_over = True

# Function to handle button clicks
def on_click(index):
    global current_player, game_over

    if board[index] == " " and not game_over:
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player, game_over
    board = [" "] * 9
    current_player = "X"
    game_over = False
    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace")

# Create buttons for the 3x3 grid
buttons = []
for i in range(9):
    print(f"Creating button for index: {i}")
    button = tk.Button(root,
                       text=" ",
                       font=("Arial", 20),
                       width=6,
                       height=3,
                       command=lambda i=i: on_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Add a reset button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

# Run the application
root.mainloop()