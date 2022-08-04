#!/usr/bin/python

 

import tkinter as tk
from tkinter import * 
import os

 

root = tk.Tk()
apps = []
my_str = 0

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApp = f.read()
        tempApp = tempApp.split(",")
        apps = [x for x in tempApp if x.strip()]

canvas1 = tk.Canvas(root, width = 500, height = 500, bg = "#263D42")
canvas1.pack()

frame = tk.Frame(root ,bg = "white" )
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

def addapp():
    for widget in frame.winfo_children():
        widget.destory()
    
    filename = filedialog.askopenfilename(initialdir = "/", title = "select file", filetypes = (("executables", "*exe"),("all files","*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()


def RunApp():
    for app in apps:
        os.startfile(app)



def hello (): 

                global my_str

                if my_str == 0:

                    label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('Futura', 18, 'italic'))

                    canvas1.create_window(250, 300, window=label1)

                    my_str=1

                else:

                    label2 = tk.Label(root, text= 'Bye World!', fg='green', font=('Futura', 18, 'italic'))

                    canvas1.create_window(250, 300, window=label2)

                    my_str=0

                    print("hello")

   

button1 = tk.Button(text='Click Me Moshe',command=hello, bg='#263D42',fg='white')

canvas1.create_window(250, 250, window=button1)

v = tk.IntVar()

openfill = tk.Button(root, text = "open fill", padx=10, pady= 5, fg="white", bg='#263D42', command = addapp)
openfill.pack()
openApps = tk.Button(root, text = "run apps", padx=10, pady= 5, fg="white", bg='#263D42', command = RunApp)
openApps.pack()


#tk.Radiobutton(root, text="One", variable=v, value=1).pack(anchor=tk.W)

#tk.Radiobutton(root, text="Two", variable=v, value=2).pack(anchor=tk.W)

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ", ")