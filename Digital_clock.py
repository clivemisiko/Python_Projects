import tkinter as tk
from tkinter import ttk
from time import strftime

# Function to update the time
def update_time():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every second

# Function to toggle between light and dark themes
def toggle_theme():
    if root["bg"] == "white":
        root.config(bg="black")
        clock_label.config(fg="white", bg="black")
        theme_button.config(text="Light Theme")
    else:
        root.config(bg="white")
        clock_label.config(fg="black", bg="white")
        theme_button.config(text="Dark Theme")

# Function to start or stop the stopwatch
def toggle_stopwatch():
    global stopwatch_running, stopwatch_time
    if stopwatch_running:
        stopwatch_running = False
        stopwatch_button.config(text="Start Stopwatch")
    else:
        stopwatch_running = True
        stopwatch_button.config(text="Stop Stopwatch")
        update_stopwatch()

# Function to update the stopwatch
def update_stopwatch():
    global stopwatch_time, stopwatch_running
    if stopwatch_running:
        stopwatch_time += 1
        hours, remainder = divmod(stopwatch_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        stopwatch_label.after(1000, update_stopwatch)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x300")
root.config(bg="white")

# Clock display
clock_label = tk.Label(root, font=("Arial", 48), fg="black", bg="white")
clock_label.pack(pady=20)

# Theme toggle button
theme_button = tk.Button(root, text="Dark Theme", font=("Arial", 12), command=toggle_theme)
theme_button.pack(pady=10)

# Stopwatch display
stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 24), fg="black", bg="white")
stopwatch_label.pack(pady=20)

# Stopwatch control button
stopwatch_running = False
stopwatch_time = 0
stopwatch_button = tk.Button(root, text="Start Stopwatch", font=("Arial", 12), command=toggle_stopwatch)
stopwatch_button.pack(pady=10)

# Start updating the time
update_time()

# Run the application
root.mainloop()