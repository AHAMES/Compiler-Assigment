# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:41:25 2019

@author: Ahmed
"""

from tkinter import *
import tkinter.messagebox

app=Tk()

app.title('GUI Example')
app.geometry('450x300+200+200')

labelText=StringVar()
labelText.set("Click Button")

lable1=Label(app,textvariable=labelText, height=4)

lable1.pack()

app.mainloop()