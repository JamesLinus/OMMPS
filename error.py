from tkinter import *
msg = Message(text="Operation Error! Please check again!")
msg.config(bg='Light Blue', font=('times', 16, 'Arial'))
msg.pack(fill=X, expand=YES)
self.button_ok = Button(self.frame,text = "ok",width = 10)
self.button_cancel = Button(self.frame,text = "cancel",width = 10)
mainloop()
