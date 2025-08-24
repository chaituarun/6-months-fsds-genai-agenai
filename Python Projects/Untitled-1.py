

import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# Create main window
root = tk.Tk()
root.geometry('400x400')
root.title('🎲 Dice Simulator Rolling Game')

# Dice image paths (adjust if they're in a subfolder)
DICE_FOLDER = "images"  # Change to "" if images are in the same folder
dice = [os.path.join(DICE_FOLDER, f'die{i}.png') for i in range(1, 7)]

# Function to load a dice image safely
def load_dice_image(path):
    try:
        image = Image.open(path)
        return ImageTk.PhotoImage(image)
    except FileNotFoundError:
        print(f"Image not found: {path}")
        return None

# Initial random dice image
initial_path = random.choice(dice)
current_dice_image = load_dice_image(initial_path)

# Heading label
heading = tk.Label(root, text="🎲 Roll the Dice!", font=("Helvetica", 18, "bold"), fg="green")
heading.pack(pady=10)

# Image label
image_label = tk.Label(root, image=current_dice_image)
image_label.image = current_dice_image  # keep reference
image_label.pack(pady=20)

# Dice rolling function
def roll_dice():
    new_path = random.choice(dice)
    new_image = load_dice_image(new_path)
    if new_image:
        image_label.configure(image=new_image)
        image_label.image = new_image  # update reference

# Roll button
roll_button = tk.Button(root, text="Roll", command=roll_dice, font=("Helvetica", 14), bg="blue", fg="white")
roll_button.pack(pady=10)

# Start GUI loop
root.mainloop()
