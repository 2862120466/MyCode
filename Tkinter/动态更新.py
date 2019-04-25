from tkinter import Tk, Checkbutton, Label, Button
from tkinter import StringVar, IntVar

root = Tk()
root.geometry('200x100')

text = StringVar()
text.set('old')
# status = IntVar()

# def change():
#     if status.get() == 1:   # if clicked
#         text.set('new')
#     else:
#         text.set('old')
#
# cb = Checkbutton(root, variable=status, command=change).pack()

def change():
    text.set('我变了')


button = Button(root, text='变', command=change).pack()

lb = Label(root, textvariable=text).pack()


root.mainloop()