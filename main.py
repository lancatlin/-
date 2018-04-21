from tkinter import *
import os
import setting
import window

class LoginWindow(Tk):
    def __init__(self):
        super().__init__()
        _font = lambda b: ('微軟正黑體', b)
        self.title('登入加分程式')
        f1 = Frame(self)
        f1.grid(row=0, column=0, padx=5, pady=5)
        Label(f1, text='班級：', font=_font(10)).grid(row=0)
        self.class_entry = Entry(f1, font=_font(10), width=20)
        self.class_entry.grid(row=0, column=1)
        f2 = Frame(self)
        f2.grid(row=1, column=0, padx=5, pady=10)
        Button(f2, text='登入', command=lambda: self.get_login(), font=_font(10)).grid(row=0, column=0, padx=5)
        Button(f2, text='設定', command=lambda: self.setting(), font=_font(10)).grid(row=0, column=1, padx=5)
        self.var = StringVar()
        self.var.set('歡迎使用加分程式')
        Label(self, textvariable=self.var, font=_font(8)).grid(row=2)

    def get_login(self):
        room = self.class_entry.get()
        if room in os.listdir():
            self.destroy()
            root = window.MainWindow(room)
            root.mainloop()
        else:
            self.var.set('輸入班級不存在')

    def setting(self):
        room = self.class_entry.get()
        self.destroy()
        setting.MainSetter(room).mainloop()

LoginWindow().mainloop()
