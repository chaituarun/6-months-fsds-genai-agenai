import tkinter as tk
import nltk
nltk.download('wordnet')

def meaning():
    
    query = str(text.get())
    synsets = wordnet.synsets(query)
    res = ''
    
    if synsets:
        # Fetch the definition of the first meaning
        for syn in synsets:
            res += f"{syn.definition()}\n"
        
        # Set and speak the output
        spokenText.set(res)
        speak("The meaning is: " + res)
    else:
        res = "Meaning not found"
        spokenText.set(res)
        speak(res)

# Creating the window 
wn = tk.Tk() 
wn.title("Senapati's Dictionary")
wn.geometry('700x500')
wn.config(bg='SlateGray1')
