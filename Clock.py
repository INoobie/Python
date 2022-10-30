import tkinter # imports
from tkinter import *
from time import strftime

_ = Tk() # basic variables
_.title('Time Clock')
__ = ('ds-digital', 100)
___ = 'black'
____ = 'cyan'
________ = 'center'
_____ = Label
___________________ = 1000
______ = _____(_, font=__, background=___, foreground=____) # making the time label
_________ = strftime('%H:%M:%S %p')
______.pack(anchor=________)

def time(): # time function
    ______.config(text=_________)
    ______.after(___________________, time)



time() # calling time

mainloop() # looping
