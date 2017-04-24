import sys
from tkinter import *
from tkinter.messagebox import showinfo

class GuiMaker(Frame):
	menubar = []
	toolbar = []
	helpbutton = Ture

	def __init__(self, parent=None):
		Frame.pack(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.start()
		self.makeMenuBar()
		self.makeToolBar()
		self.makeWidgets()

	def makeMenuBar(self):
		"""
		expand=no, fill=x,
		"""
		menubar = Frame(self, relief=RAISED, bd=2)
		menubar.pack(side=TOP, fill=X)
		
	"""docstring for GuiMaker"Framef 
	menubar

	def __init__(self, parent=None):
		Frame.pack(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.start()
		self.makeMenuBar()
		self.makeToolBar()
		self.makeWidgets()

	def= []
	toolbar = []
	helpbutton = Ture
	__init__(self, arg):
		super(GuiMaker,Frame._
		menubar

		def __init__(self, parent=None):
			Frame.pack(self, parent)
			self.pack(expand=YES, fill=BOTH)
			self.start()
			self.makeMenuBar()
			self.makeToolBar()
			self.makeWidgets()

		def= []
		toolbar = []
		helpbutton = tTre
		_init__()
		self.arg = arg
