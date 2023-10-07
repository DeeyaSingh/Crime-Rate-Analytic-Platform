import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import os
window = Tk()
def karnataka():
     os.system('karnataka_crimes.py')
def nagaland():
     os.system('nagaland_crimes.py')
def uttarpradesh():
     os.system('up_crimerate.py')
def compare():
     os.system('total.py')
window.title("crime rate analysis") 
window.geometry('350x200') 
lbl = Label(window, text="select location")
lbl.grid(column=0, row=0) 
btn1 = Button(window, text="karnataka",command=karnataka,width=15)
btn2 = Button(window, text="nagaland",command=nagaland,width=15)
btn3 = Button(window, text="uttarpradesh",command=uttarpradesh,width=15)
btn4 = Button(window, text="compare the three",command=compare,width=15)
btn1.grid(column=0, row=2)
btn2.grid(column=0, row=4)
btn3.grid(column=0, row=6)
btn4.grid(column=0, row=8)
window.mainloop()
