
import tkinter as tk
import tkinter.messagebox as mb
import lyricsgenius

# Replace with your Genius API token
GENIUS_API_TOKEN = "your_access_token_here"
genius = lyricsgenius.Genius(GENIUS_API_TOKEN)

def extract_lyrics():
    artist_name = artist.get()
    song_name = song.get()

    try:
        song_obj = genius.search_song(song_name, artist_name)
        if song_obj and song_obj.lyrics:
            print(song_obj.lyrics)
            mb.showinfo("Lyrics Extracted", "Lyrics have been printed in the terminal.")
        else:
            mb.showerror("Lyrics Not Found", "Could not find lyrics for that song.")
    except Exception as e:
        mb.showerror("Error", f"An error occurred:\n{str(e)}")

# --- UI Setup ---
root = tk.Tk()
root.title("Song Lyrics Extractor")
root.geometry("600x200")
root.resizable(False, False)
root.config(bg='CadetBlue')

tk.Label(root, text="Song Lyrics Extractor", font=("Comic Sans MS", 16, 'bold'), bg='CadetBlue').pack(side=tk.TOP, fill=tk.X)

tk.Label(root, text='Enter the song name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=50)
song = tk.StringVar()
tk.Entry(root, width=40, textvariable=song, font=('Times New Roman', 14)).place(x=200, y=50)

tk.Label(root, text="Enter the artist's name: ", font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=100)
artist = tk.StringVar()
tk.Entry(root, width=40, textvariable=artist, font=('Times New Roman', 14)).place(x=200, y=100)

tk.Button(root, text='Extract lyrics', font=("Georgia", 10), width=15, command=extract_lyrics).place(x=220, y=150)

root.mainloop()
