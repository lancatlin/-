from tkinter import *
import os


def encode(s, x):
    code = s
    T_code = ''
    for i in code:
        T_code += chr(ord(i) - x)
    return T_code


class login(Tk):
    def __init__(self):
        super().__init__()
        self.start = False
        self.room = None

        _font = lambda b: ('微軟正黑體', b)
        self.geometry('300x200')
        self.title('login')
        Label(self, text='班級：', font=_font(10)).grid(row=0, padx=5, pady=15)
        self.class_entry = Entry(self, font=_font(10), width=20)
        self.class_entry.grid(row=0, column=1)
        Label(self, text='輸入密碼:', font=_font(10)).grid(row=1, column=0)
        self.entry = Entry(self, font=_font(10), width=20, show='*')
        self.entry.grid(column=1, row=1)
        self.entry.bind('<Return>', lambda x:self.get_login())
        Button(self, text='登入', command=self.get_login, font=_font(10)).grid(row=2, column=0)
        Button(self, text='設定', command=lambda: os.system('start command python creat.py'), font=_font(10)).grid(
            row=2, column=1)
        self.var = StringVar()
        self.var.set('歡迎使用加分程式')
        Label(self, textvariable=self.var, font=_font(8)).grid(row=3, columnspan=2)

    def mainloop(self, n=0):
        while True:
            if self.start:
                self.destroy()
                return self.room
            else:
                self.update()
                self.update_idletasks()

    def get_login(self):
        room = self.class_entry.get()
        x = 10
        try:
            f = open(room+'//code.sc', 'r')
            self.code = encode(f.read(), x)
        except FileNotFoundError:
            self.code = ''

        if self.entry.get() != self.code:
            self.entry.delete(0, 'end')
            self.var.set('密碼或班級錯誤，請再試一次')
        elif self.class_entry.get() not in os.listdir():
            self.var.set('輸入班級不存在')
        else:
            self.room = self.class_entry.get()
            self.start = True


if __name__ == '__main__':
    boot = login()
    boot.wait_login()