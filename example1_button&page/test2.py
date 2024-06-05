from tkinter import *
import time
import threading


class Application(Frame):
    """Build the basic window frame template"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        self.lable1 = Label(self, text=current_time)
        self.lable1.grid(row=0, column=0, sticky=NSEW)
        self.lable1.config(font=('Arial', 100))
        self.lable1.config(bg='black', fg='white')
        self.lable1.after(1000, self.Refresher)

    def Refresher(self):
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        self.lable1.configure(text=current_time)
        self.lable1.after(1000, self.Refresher)


root = Tk()
root.title('Test Application window with label1')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.config(bg='black')
app = Application(root)
app.mainloop()

