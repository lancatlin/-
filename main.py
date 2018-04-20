from tkinter import *
import login

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('加分程式')

    def setPath(self, path):
        self.path = path

root = MainWindow()
top = login.LoginWindow(root)
top.mainloop()
root.mainloop()
