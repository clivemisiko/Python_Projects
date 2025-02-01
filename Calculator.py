import tkinter as tk

# Function to handle button clicks
def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))  # Evaluate the expression
            entry.delete(0, tk.END)  # Clear the entry field
            entry.insert(tk.END, result)  # Display the result
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    else:
        entry.insert(tk.END, text)  # Add the button's text to the entry field

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")  # Set the window size

# Create an entry widget to display the input and results
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

# Define the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

# Add buttons to the frame
for i, text in enumerate(buttons):
    button = tk.Button(button_frame, text=text, font=("Arial", 15), relief=tk.RAISED, borderwidth=2)
    button.grid(row=i // 4, column=i % 4, sticky="nsew", padx=5, pady=5)
    button.bind("<Button-1>", button_click)  # Bind the click event to the button

# Configure the grid to expand evenly
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
    button_frame.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()