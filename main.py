from tkinter import *
from tkinter.filedialog import askopenfilename
import pdfplumber
import os
from gtts import gTTS


text = ""

def open_file():
    # this function takes file from user.
    file_location = askopenfilename()
    return file_location


def working():
    global text
    file_location = open_file()
    name = os.path.basename(file_location)
    file_name = os.path.splitext(name)

    with pdfplumber.open(file_location) as data:
        for line in data.pages:
            clear_text = line.extract_text()
            text += clear_text
    audio_file = gTTS(text=text, lang="en")
    audio_file.save(f"Audio {file_name[0]}.mp3")
    print("done")

#Build interface.
window = Tk()
window.title("Pdf to Audio converter")
window.geometry("300x100")
window.config(bg="navajowhite")

button = Button(text="Open file", bg="navajowhite", fg="black", highlightthickness=0,
                highlightbackground="navajowhite", width=20, command=working)
button.place(x=50, y=30)

window.mainloop()
