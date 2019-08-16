#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import random
import gaugelib


win = tk.Tk()
#a5 = PhotoImage(file="faisal.png")
#win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("Ardiotech Raspberry Pi Version 2.0")
win.geometry("800x400+0+0")
win.resizable(width=True, height=True)
win.configure(bg='white')

g_value=0
x=0

def read_every_second():
    global x
    g_value=random.randint(0,30)
    p1.set_value(int(10))

    x+=1    
    if x>100:
#        graph1.draw_axes()
        x=0
    win.after(100, read_every_second)

p1 = gaugelib.DrawGauge2(
    win,
    max_value=300.0,
    min_value=0.0,
    size=300,
    bg_col='white',
    unit = "Temperature",bg_sel = 4)
p1.place(x=300,y=100)
#p1.pack()

read_every_second()
mainloop()
