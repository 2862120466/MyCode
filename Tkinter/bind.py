from tkinter import *

top = Tk()

def call_back(event):
    print( event.x, event.y )

top.bind( '<Button-1>', call_back )

help(Tk.bind)

mainloop()

