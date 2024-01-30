# https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *

root = Tk()

e = Entry(root, width=50,bg="yellow",fg="blue",borderwidth=5)
e.grid(row=4,column=0)
e.insert(0,"Enter Your Name")



def myClick():
    hello = "Hello " + e.get()
    myLabel1 = Label(root, text= hello)
    myLabel1.grid(row=0,column=0)



myButton = Button(root,text="Enter Your Name!",padx=50,pady=50, command=myClick, fg="blue",bg="green",borderwidth=5)
myButton.grid(row=3,column=1)

myLabel2 = Label(root, text="My Name is Scott")


myLabel2.grid(row=1,column=1)


root.mainloop()