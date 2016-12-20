#!/usr/bin/python

import tkinter

def getSub():
	sub = tkinter.Tk()
	sub.mainloop()
top = tkinter.Tk()
button = tkinter.Button(top, text='Hello', command=getSub)
button.pack()
top.mainloop()

