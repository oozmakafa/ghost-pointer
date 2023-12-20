import pyautogui
import random
import time

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Number of random movements
num_movements = 10

for _ in range(num_movements):
    # Generate random coordinates within the screen boundaries
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    
    # Move the mouse cursor to the random coordinates
    pyautogui.moveTo(x, y, duration=0.5)
    
    # Pause for a moment before the next movement
    time.sleep(40)
