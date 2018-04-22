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
<<<<<<< HEAD
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
=======
        f2.grid(row=1, column=2, padx=5, sticky=N)

        f21 = Frame(f2)
        f21.pack()
        Label(f21, text='歷史', font=_font(20)).grid(row=0)
        self.history = Listbox(f21, width=10, height=15, font=_font(20))
        self.history.grid(row=1)
        for i in self.data.history:
            self.history.insert(END, i)
        day = time.strftime('%H.%m/%d', time.localtime())
        self.history.insert(0, day)
        sb3 = Scrollbar(f21)
        sb3.grid(row=1,sticky=N + W*self.system + S + E)
        self.history.configure(yscrollcommand=sb3.set)
        sb3.configure(command=self.history.yview)

        if self.team:
            self.history['height'] = 5
            f22 = Frame(f2)
            f22.pack()
            Label(f22,text='小組分數',font=_font(20)).grid(row=0)
            self.teamlist = Listbox(f22,listvariable=self.team,width=10,height=9,font=_font(20))
            self.teamlist.grid(row=1)
            sb2 = Scrollbar(f22)
            sb2.grid(row=1, sticky=N + W*self.system + S + E)
            self.teamlist.configure(yscrollcommand=sb2.set)
            sb2.configure(command=self.teamlist.yview)

        #第三區塊
        f3 = Frame(self)
        f3.grid(row=1,column=3,padx=20)
        #第三之一區塊
        f31 = Frame(f3)
        f31.pack()
        self.entry = Entry(f31,width=6,font=_font(30))
        self.entry.grid(row=1,sticky=N)
        self.entry.bind('<Return>',lambda x:self.button_up())
        
        f32 = Frame(f3)
        f32.pack()
        self.button=['1', '2', '3', '4', '5', '6', '7', '8', '9', 'C', '0', '回復','扣分','加分', '+']
        for i in range(len(self.button)):
            Button(f32, text=self.button[i], width=4, height=1, font=_font(30), \
                    command=lambda x=self.button[i]:self.button_up(x))\
                    .grid(row=i//3, column=i%3, padx=9, pady=10)
        self.update()

    def button_up(self, b='加分'):
        if b == 'C':
            self.entry.delete(0, 'end')
        elif b == '回復':
            string = self.history.get(0)
            if '+' in string:
                string = string.replace('+', '-')
            elif '-' in string:
                string = string.replace('-', '+')
            else:
                self.history.delete(0)
                return None
            self.add_point(string)
            self.history.delete(0,1)
            self.data.write(self.history.get(0, 'end'))
            self.button_up('C')
        elif b == '加分':
            string = self.entry.get()    
            if not ('+' in string or '-' in string):
                string += '+1'
            self.add_point(string)
            self.button_up('C')
            self.update()
        elif b == '扣分':
            string = self.entry.get()
            if '+' in string:
                string = string.replace('+', '-')
            else:
                string += '-1'
            self.add_point(string)
            self.button_up('C')
            self.update()

        else:
            self.entry.insert('end', b)

    def add_point(self, string):
        if '+' in string:
            n, plus = string.split('+')
        elif '-' in string:
            n, plus = string.split('-')
            plus = '-'+plus
        if self.data.update(int(n), int(plus)):
            self.history.insert(0, string)
            self.data.write(self.history.get(0, 'end'))
            self.update()
            self.scorelist.see(int(n)-1)
>>>>>>> d2109ac959d456f4449ba9f875f2f793d5f6397f
        else:
            self.var.set('輸入班級不存在')

    def setting(self):
        room = self.class_entry.get()
        self.destroy()
        setting.MainSetter(room).mainloop()

LoginWindow().mainloop()
