import tkinter

window = tkinter.Tk()
window.title("Scott Made this!")

# creating a function called say_hi()
def say_hi():
    tkinter.Label(window, text = "HI").pack()

def left_click(event):
    tkinter.Label(window, text = "Left CLick!").pack()

def middle_click(event):
    tkinter.Label(window, text = "Middle CLick!").pack()

def right_click(event):
    tkinter.Label(window, text = "Right CLick!").pack()

window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)


# creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")

# now, create some widgets in the top_frame and bottom_frame
btn1 = tkinter.Button(top_frame, text="Button1", fg= "red").pack()# 'fg - foreground' is used to color the conents
btn2 = tkinter.Button(top_frame, text="Button2", fg= "green").pack()# 'text' is used to write the text on the button
btn3 = tkinter.Button(bottom_frame, text="Button2", fg= "purple").pack(side="left")#'side' is used to align the  widgets
btn4 = tkinter.Button(bottom_frame, text="Button2", fg= "orange").pack(side='left')#
Hi_button = tkinter.Button(bottom_frame, text="Click Me!", fg= "orange", command= say_hi).pack(side='left')#




window.mainloop()