from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import tk_tools
import csv


root = Tk()
root.title("Combine UI")
root.iconbitmap("Images/BensonHillIngredients.ico")
width = 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
#root.resizable(0, 0)


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
frame_guages = LabelFrame(root, text="Guages", padx=5, pady=5)
frame_guages.pack(padx=10, pady=10)

frame_table = LabelFrame(root, text="Polytec Output File", padx=5, pady=5)
frame_table.pack(padx=10, pady=10)


#Guages
s_gauge = tk_tools.Gauge(frame_guages, max_value=20.0, label=' S_Value', unit='S')
s_gauge.pack(side=RIGHT)
s_gauge.set_value(10)


h_gauge = tk_tools.Gauge(frame_guages, max_value=100.0, label=' H_Value', unit='H')
h_gauge.pack(side=RIGHT)
h_gauge.set_value(10)


protein_gauge = tk_tools.Gauge(frame_guages, max_value=100.0, label=' Protein_Value', unit='Protein')
protein_gauge.pack(side=RIGHT)
protein_gauge.set_value(10)








TableMargin = Frame(frame_table, width=500)
TableMargin.pack(side=BOTTOM)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Timestamp", "H", "S", "Protein"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
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
with open('C:/Users/shendricks/OneDrive - Benson Hill/Documents/Tkinter/tkinter-tutorial-/Combine_UI/ResultsCSV.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        my_tag='normal'
        TimeStamp = row['TimeStamp']
        H_value = row['H']
        S_value = row['S']
        Protein_value = row['Protein']

        if(int(H_value) > 60):
            my_tag = 'bad'

    
        tree.insert("", 0, values=(TimeStamp, H_value, S_value, Protein_value), tags=(my_tag))


tree.pack()
# with open('C:/Users/shendricks/OneDrive - Benson Hill/Documents/Tkinter/tkinter-tutorial-/Combine_UI/ResultsCSV.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=',')
#     #for row in csv_reader:


    


#Table insert
#treeview = ttk.Treeview(columns=())













root.mainloop()