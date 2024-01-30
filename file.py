from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("Learning to Code")
root.iconbitmap("Images/BensonHillIngredients.ico")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="Images", title="Select A File", filetypes=(("jpg", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text=str(root.filename))
    my_label.pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.pack()



my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()

#"C:/Users/shendricks/OneDrive - Benson Hill/Documents/Tkinter/tkinter-tutorial-/Images"