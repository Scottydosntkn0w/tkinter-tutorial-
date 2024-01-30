from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learing to Code")
root.iconbitmap("Images/BensonHillIngredients.ico")

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="dont click here")
b.grid(row=0, column=0)


root.mainloop()