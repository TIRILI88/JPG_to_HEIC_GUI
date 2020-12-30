from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import pipreqs

import os


def find_file():
    dir_finder = filedialog.askdirectory()
    input.insert(END, dir_finder)


def convert():
    location = input.get()

    if len(location) == 0:
        messagebox.showwarning(title="Requirements", message="Not all requirements met!")

    else:
        counter = 0
        for i in os.listdir(location):
            files = os.path.join(location, i)
            split = os.path.splitext(files)
            if split[1] =='.HEIC':
               os.rename(files, split[0]+'.JPG')
               counter += 1

        messagebox.showinfo(title="All files converted", message=f"{counter} files successfully converted")



window = Tk()
window.title("HEIC to JPEG Converter")
window.config(padx=20, pady=50)

canvas = Canvas(width=150, height=150)
img = Image.open("./heic.png")
img = img.resize((150, 150), resample=0)
img = ImageTk.PhotoImage(img)
canvas.create_image(80, 80, image=img)
canvas.grid(row=0, column=0, columnspan=2)


# Label
label = Label(text="Enter the folder of the pictures: ", font=("Calibri", 14, "normal"))
label.grid(row=1, column=0)


# Entry
input = Entry(width=35)
input.grid(row=1, column=1)
input.focus()


# Button
find_file_button = Button(text="⬇️", command=find_file)
find_file_button.grid(row=1, column=2)

button = Button(text="Convert", width=40, command=convert)
button.grid(row=2, column=1, columnspan=2)


window.mainloop()