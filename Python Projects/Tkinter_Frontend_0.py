


import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("200x100")

def say_hell0():
    print("Hello, world")
    print('good bye')
    
hello_button = tk.Button(root, text= "click me", command=say_hell0)
hello_button.pack(pady=20)

root.mainloop()
