#-*- coding:utf-8 -*-

from tkinter import *
import platform
import time

import data
import login


class MyWindow(Tk):
    def __init__(self, path):
        super().__init__()
        self.title(path+'加分程式')
        self.geometry('1000x800')
        self.data = data.Data(path)
        self.score = StringVar()
        if self.data.team:
            self.team = StringVar()
        else:
            self.team = None
        if platform.system() == 'Linux':
            self.system = 0
        else:
            self.system = 1

        _font = lambda b: ('微軟正黑體',b) #字體設定
        #第一區塊
        f1 = Frame(self)
        f1.grid(row=1,column=1,padx=15,sticky=N)
        Label(f1,text='分數',font=_font(20)).grid(row=0)
        
        self.scorelist = Listbox(f1, listvariable=self.score, \
                width=10, height=15, font=_font(20))
        self.scorelist.grid(row=1)
        sb = Scrollbar(f1)
        sb.grid(row=1,sticky=N+W*self.system+S+E)
        self.scorelist.configure(yscrollcommand=sb.set)
        sb.configure(command=self.scorelist.yview)
        
        #第二區塊
        f2 = Frame(self)
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
        else:
            self.entry.delete(0, END)

    def update(self):
        score, team = self.data.get()
        self.score.set(score)
        if self.team:
            self.team.set(team)
l = login.login()
room = l.mainloop()
window = MyWindow(room)
window.mainloop()

