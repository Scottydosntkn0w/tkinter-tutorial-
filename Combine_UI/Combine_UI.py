from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import tk_tools
import csv
from tkinter import filedialog
import os


class Monkey(object):
    def __init__(self):
        self._cached_stamp = 0
        self.filename = '/path/to/file'

    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...

root = Tk()
root.title("Combine UI")
root.iconbitmap("Images/BensonHillIngredients.ico")
width = 1400
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
#root.resizable(0, 0)

def file_open():
    global file_time__label
    global file_path__label
    root.filename = filedialog.askopenfilename(initialdir="Combine_UI", title="Select A File", filetypes=(("csv", "*.csv"),("all files", "*.*")))
    file_time__label['text'] = ""
    file_path__label['text'] = ""
    file_path__label.pack(side=LEFT)
    file_time__label.pack(side=LEFT)


    file_path__label = Label(frame_file_nav, text=str(root.filename))
    file_path__label.pack(side=LEFT)

    file_time_change = os.stat(root.filename).st_mtime
    file_time__label = Label(frame_file_nav, text=file_time_change)
    file_time__label.pack(side=LEFT)

    my_tag='normal'
    try:
        with open(file_path__label['text']) as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                my_tag='normal'
                TimeStamp = row['TimeStamp']
                H_value = row['H']
                S_value = row['S']
                Protein_value = row['Protein']

                if(int(H_value) > 60):
                    my_tag = 'bad'

                protein_gauge.set_value(Protein_value)
                h_gauge.set_value(H_value)
                s_gauge.set_value(S_value)

                tree.insert("", 0, values=(TimeStamp, H_value, S_value, Protein_value), tags=(my_tag))
    except Exception as e:
        print(e)

# Add some style
style = ttk.Style()
#Pick a theme
style.theme_use("default")
#Configure our Tree view colors
style.configure("Treeview",
                background = "silver",
                foreground="black",
                rowheight=25,
                fieldbackground="silver",
                font=("Helvetica", "16")
                )

# Change selected color
# style.map('Treeview',
#           background=[('selected', 'blue')])



frame_file_nav = LabelFrame(root, text="Select File", padx=5, pady=5)
frame_file_nav.pack(padx=10, pady=10)

get_file_btn = Button(frame_file_nav, text="Select", command=file_open)
get_file_btn.pack(side=LEFT)
file_path__label = Label(frame_file_nav, text=str('C:/Users/shendricks/OneDrive - Benson Hill/Documents/Tkinter/tkinter-tutorial-/Combine_UI/ResultsCSV.csv'))
file_path__label.pack(side=LEFT)
file_time_change = os.stat('C:/Users/shendricks/OneDrive - Benson Hill/Documents/Tkinter/tkinter-tutorial-/Combine_UI/ResultsCSV.csv').st_mtime
file_time__label = Label(frame_file_nav, text=file_time_change)
file_time__label.pack(side=LEFT)

frame_guages = LabelFrame(root, text="Guages", padx=5, pady=5)
frame_guages.pack(padx=10, pady=10)

frame_table = LabelFrame(root, text="Polytec Output File", padx=5, pady=5)
frame_table.pack(padx=10, pady=10)



#file open components

get_file_btn = Button(root, text="Open File", command=open)
get_file_btn.pack()
file_path__label = Label(root, text=str('C:/Users/shendricks/OneDrive - Benson Hill/Documents/Tkinter/tkinter-tutorial-/Combine_UI/ResultsCSV.csv'))
file_path__label.pack()



#Guages
protein_gauge = tk_tools.Gauge(frame_guages,width= 400, height= 200, max_value=100.0, label=' Protein_Value', unit='',divisions=10,yellow=75,red=90,yellow_low=20,red_low=10,bg='lightgrey')
protein_gauge.pack(side=RIGHT)
protein_gauge.set_value(10)

s_gauge = tk_tools.Gauge(frame_guages, width= 400, height= 200,min_value=0, max_value=20.0, label=' S_Value', unit='',divisions=10,yellow=50,red=50,yellow_low=0,red_low=0,bg='lightgrey')
s_gauge.pack(side=RIGHT)
s_gauge.set_value(10)


h_gauge = tk_tools.Gauge(frame_guages,width= 400, height= 200, max_value=120.0, label=' H_Value', unit='',divisions=10,yellow=50,red=50,yellow_low=0,red_low=0,bg='lightgrey')
h_gauge.pack(side=RIGHT)
h_gauge.set_value(10)




#treeview Table

TableMargin = Frame(frame_table, width=500)
TableMargin.pack(side=BOTTOM)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Timestamp", "H", "S", "Protein"), height=400, selectmode="none", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Timestamp', text="Timestamp", anchor=W)
tree.heading('H', text="H", anchor=W)
tree.heading('S', text="S", anchor=W)
tree.heading('Protein', text="Protein", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=150)
tree.column('#2', stretch=NO, minwidth=0, width=50)
tree.column('#3', stretch=NO, minwidth=0, width=50)
tree.column('#4', stretch=NO, minwidth=0, width=50)

tree.tag_configure('good',background="green")
tree.tag_configure('bad', background="red")

my_tag='normal'
try:
    with open(file_path__label['text']) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            my_tag='normal'
            TimeStamp = row['TimeStamp']
            H_value = row['H']
            S_value = row['S']
            Protein_value = row['Protein']

            if(int(H_value) > 60):
                my_tag = 'bad'

            protein_gauge.set_value(Protein_value)
            h_gauge.set_value(H_value)
            s_gauge.set_value(S_value)

            tree.insert("", 0, values=(TimeStamp, H_value, S_value, Protein_value), tags=(my_tag))
except Exception as e:
    print(e)


tree.pack()





















root.mainloop()