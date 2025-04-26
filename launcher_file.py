from tkinter import *
from tkinter.ttk import *
import os
import sys
from subprocess import check_call
import subprocess

master = Tk()
master.geometry("400x400")


# model 1
def openNewWindow1():
    newWindow = Toplevel(master)
    newWindow.title("Custom")
    newWindow.geometry("400x400")
    btn11 = Button(newWindow,
                   text="Only Eyes",
                   command=run11)
    btn11.pack(pady=10)

    btn12 = Button(newWindow,
                   text="Only Yawn",
                   command=run12)
    btn12.pack(pady=10)

    btn13 = Button(newWindow,
                   text="Both Eyes and Yawn",
                   command=run13)
    btn13.pack(pady=10)


#     Label(newWindow,
#           text ="What you want to detect in Model 1").pack()
# btn=Button()

# model 2
def openNewWindow2():
    newc = Toplevel(master)
    # new2 = TopLevel(master)
    newc.title("VGG16")
    newc.geometry("400x400")
    btn11 = Button(newc,
                   text="Only Eyes",
                   command=run21)
    btn11.pack(pady=10)

    btn12 = Button(newc,
                   text="Only Yawn",
                   command=run22)
    btn12.pack(pady=10)

    btn13 = Button(newc,
                   text="Both Eyes and Yawn",
                   command=run23)
    btn13.pack(pady=10)


#     Label(newc,
#          text ="What you want to detect in Model 2").pack()
# model 2
def openNewWindow3():
    new3 = Toplevel(master)
    new3.title("VGG19")
    new3.geometry("400x400")
    btn11 = Button(new3,
                   text="Only Eyes",
                   command=run31)
    btn11.pack(pady=10)

    btn12 = Button(new3,
                   text="Only Yawn",
                   command=run32)
    btn12.pack(pady=10)

    btn13 = Button(new3,
                   text="Both Eyes and Yawn",
                   command=run33)
    btn13.pack(pady=10)


#     Label(new3,
#          text ="What you want to detect in Model 3").pack()

# main window
label = Label(master, text="Main")
label.pack(pady=10)


def run11():
    os.system('python Custom\kaggle_eye.py')


def run12():
    os.system('python Custom\kaggle_mouth.py')


def run13():
    os.system('python Custom\kaggle_both.py')


def run21():
    os.system('python VGG16\VGG16_eye.py')


def run22():
    os.system('python VGG16\VGG16_mouth.py')


def run23():
    os.system('python VGG16\VGG16_both.py')


def run31():
    os.system('python VGG19\VGG19_eye.py')


def run32():
    os.system('python VGG19\VGG19_mouth.py')


def run33():
    os.system('python VGG19\VGG19_both.py')


btn = Button(master,
             text="Custom",
             command=openNewWindow1)
btn.pack(pady=10)
btn2 = Button(master,
              text="VGG16",
              command=openNewWindow2)
btn2.pack(pady=10)
btn3 = Button(master,
              text="VGG19",
              command=openNewWindow3)
btn3.pack(pady=10)

master.mainloop()