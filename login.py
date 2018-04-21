from tkinter import *
import os
import setting

class LoginWindow(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        _font = lambda b: ('微軟正黑體', b)
        self.geometry('300x200')
        self.title('登入加分程式')
        Label(self, text='班級：', font=_font(10)).grid(row=0, padx=5, pady=15)
        self.class_entry = Entry(self, font=_font(10), width=20)
        self.class_entry.grid(row=0, column=1)
        Button(self, text='登入', command=lambda: self.get_login(root), font=_font(10)).grid(row=2, column=0)
        Button(self, text='設定', command=lambda: self.setting(root), font=_font(10)).grid(
            row=2, column=1)
        self.var = StringVar()
        self.var.set('歡迎使用加分程式')
        Label(self, textvariable=self.var, font=_font(8)).grid(row=3, columnspan=2)

    def get_login(self, root):
        room = self.class_entry.get()
        if room in os.listdir():
            root.begin(room)
            self.withdraw()
        else:
            self.var.set('輸入班級不存在')

    def setting(self, root):
        room = self.class_entry.get()
        self.withdraw()
        setter = setting.MainSetter(root, room)
        setter.mainloop()

