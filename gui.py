import tkinter as tk

 = "hello world\n(click me)"
 self.hi.there["command"] = self.say_hi
 self.hi_thereclass Application(tk.Frame):
	def __init__ (self, master-none);
	    super().__init__(master)
	    self.pack()
	    self.create_widgets()

	def create_widgets(self);

	    self.hi_there = tk.Button(self)
	    self.hi_there["text"] = "hello world\n(click me)"
	    self.hi_there["command"] = self.say_hi
	    self.hi_there.pack(side="top")


	    self.quit = tk.Button(self, text="QUIT", fg="red",
	    	                  command=root.destroy)
	    self.quit.pack(side="bottom")

	def say_hi(self):
		print("hi there, evertone !")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
	"""docstring for Application"tk.Framef 
	def __init__ (self, master-none);
	    super().__init__(master)
	    self.pack()
	    self.create_widgets()

	def create_widgets(self);

	    self.hi_there = tk.Button(self)
	    self.hi.there["text"]__ini = "hello world\n(click me)"
	    self.hi.there["command"] = self.say_hi
	    self.hi_theret__(self, arg):
		super(Application,tk.Frame._
		def __init__ (self, master-none);
		    super().__init__(master)
		    self.pack()
		    self.create_widgets()

		def create_widgets(self);

		    self.hi_there = tk.Button(self)
		    self.hi.there["text"]_init__()
		self.arg = arg
