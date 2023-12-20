import pyautogui
import random
import time
import tkinter as tk
import threading

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Initialize toggle variable and default sleep duration
is_running = False
sleep_duration = 30  # Default sleep duration set to 30 seconds

def toggle():
    global is_running
    if is_running:
        is_running = False
        status_label.config(text="Status: Off")
    else:
        is_running = True
        status_label.config(text="Status: On")
        threading.Thread(target=move_mouse, daemon=True).start()

def set_sleep(val):
    global sleep_duration
    sleep_duration = int(val)
    sleep_label.config(text=f"Sleep duration: {sleep_duration} seconds")

def move_mouse():
    global is_running, sleep_duration
    while is_running:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=.5)
        time.sleep(sleep_duration)

def on_closing():
    global is_running
    is_running = False
    root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("Ghost Pointer")

toggle_button = tk.Button(root, text="Toggle", command=toggle)
toggle_button.pack(pady=10)

status_label = tk.Label(root, text="Status: Off")
status_label.pack()

sleep_scale = tk.Scale(root, from_=5, to=60, orient=tk.HORIZONTAL, label="Sleep Duration (seconds)", command=set_sleep)
sleep_scale.set(sleep_duration)
sleep_scale.pack()

sleep_label = tk.Label(root, text=f"Sleep duration: {sleep_duration} seconds")
sleep_label.pack()

# Handle closing of the window
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the GUI main loop
root.mainloop()
