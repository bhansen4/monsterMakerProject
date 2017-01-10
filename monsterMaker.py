#!/usr/bin/python

from tkinter import *

master = Tk()
pageName = 'File'

#Menu Objects
mainMenu = Menu(master)

mainMenu.add_command(label="File", command=None)

templateMenu = Menu(mainMenu, tearoff=0)
templateMenu.add_command(label="New", command=None)
templateMenu.add_command(label="Edit", command=None)
templateMenu.add_command(label="Delete", command=None)
mainMenu.add_cascade(label="Templates", menu=templateMenu)

generatorMenu = Menu(templateMenu, tearoff=0)
generatorMenu.add_command(label="New", command=None)
#generatorMenu.add_command(label="Edit", command=None)
#generatorMenu.add_command(label="Import", command=None)
mainMenu.add_cascade(label="Generator", menu=generatorMenu)

mainMenu.add_command(label="Quit", command=quit)
master.config(menu = mainMenu)

buttonTemplate = Button(master, text='Format Template', command=printStuff)
buttonTemplate.grid(row = 0)
buttonCreature = Button(master, text='Generate Creature')
buttonCreature.grid(row = 1)
entry = Entry(master)
entry.grid(row = 2)

#New Template Objects
buttonSaveTemplate = Button(master, text='Save Template', command=printStuff)
buttonVerifyTemplate = Button(master, text='Verfiy Template', command=printStuff)
buttonStatTemplate = Button(master, text='Add Stat', command=printStuff)
#Edit Template Objects
#Delete Template Objects
#New Generator Objects


def printStuff():
	print('stuff')

def menu():
	mainMenu = Menu(master)
	
	mainMenu.add_command(label="File", command=None)
	
	templateMenu = Menu(mainMenu, tearoff=0)
	templateMenu.add_command(label="New", command=None)
	templateMenu.add_command(label="Edit", command=None)
	templateMenu.add_command(label="Import", command=None)
	mainMenu.add_cascade(label="Templates", menu=templateMenu)
	
	generatorMenu = Menu(templateMenu, tearoff=0)
	generatorMenu.add_command(label="New", command=None)
	generatorMenu.add_command(label="Edit", command=None)
	generatorMenu.add_command(label="Import", command=None)
	mainMenu.add_cascade(label="Generator", menu=generatorMenu)
	
	mainMenu.add_command(label="Quit", command=quit)
	master.config(menu = mainMenu)

def setPage(pageName):
	print(pageName)
	'''
	pageName = Label(master, text=pageName)
	pageName.grid()
	'''

def quit():
	master.destroy()

def initial(pageName):
	#pageName = Label(master, text=pageName)
	#pageName.grid(row = 0)
	def printStuff():
		print('stuff')
	buttonTemplate = Button(master, text='Format Template', command=printStuff)
	buttonTemplate.grid(row = 0)
	buttonCreature = Button(master, text='Generate Creature')
	buttonCreature.grid(row = 1)
	entry = Entry(master)
	entry.grid(row = 2)


menu()
master.title("Monster Maker")
master.minsize(width=500, height=500)
master.maxsize(1000, 1000)
master.mainloop()