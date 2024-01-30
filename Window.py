from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Learning to Code")
root.iconbitmap("Images/BensonHillIngredients.ico")


def open():
    global my_img
    top = Toplevel()
    top.title("second Window")
    top.iconbitmap("Images/BensonHillIngredients.ico")
    my_img = ImageTk.PhotoImage(Image.open("Images\Combine.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()    



btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()