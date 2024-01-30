from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("Learning to Code")
root.iconbitmap("Images/BensonHillIngredients.ico")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this Box", variable=var, onvalue="Pizza", offvalue="Hamburger")
c.deselect()
c.pack()


myButton = Button(root, text="My Selection", command=show).pack()

root.mainloop()
