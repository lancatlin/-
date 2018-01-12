#window
#cmd /k cd C:\Users\Lin\Google 雲端硬碟\python\AddPoints & python "$(FULL_CURRENT_PATH)" &PAUSE&EXIT
from tkinter import *
import data,login,platform
import time


class mywindow(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.var = StringVar()
        self.data = data.score_manager()
        self.teen_manager = data.teen(self.data)
        self.history_manager = data.history()
        if self.teen_manager.mode:
            self.teen = StringVar()
        if platform.system() == 'Linux':
            self.system = 0
        else:
            self.system = 1
        self.setupUI()
    def setlist(self):
        self.var.set(self.data.get())
        if self.teen_manager.mode:
            self.teen.set(self.teen_manager.get())
    def setupUI(self):
        _font = lambda b: ('微軟正黑體',b) #自體設定
        #第一區塊
        f1 = Frame(self)
        f1.grid(row=1,column=1,padx=15,sticky=N)
        Label(f1,text='分數',font=_font(20)).grid(row=0)
        
        self.scorelist = Listbox(f1,listvariable=self.var,width=10,height=15,font=_font(20))
        self.scorelist.grid(row=1)
        sb = Scrollbar(f1)
        sb.grid(row=1,sticky=N+W*self.system+S+E)
        self.scorelist.configure(yscrollcommand=sb.set)
        sb.configure(command=self.scorelist.yview)
        #第二區塊
        f2 = Frame(self)
        f2.grid(row=1,column=2,padx=5,sticky=N)

        f21 = Frame(f2)
        f21.pack()
        Label(f21, text='歷史', font=_font(20)).grid(row=0)
        self.history = Listbox(f21,width=10,height=15,font=_font(20))
        self.history.grid(row=1)
        for i in self.history_manager.read():
            self.history.insert(END, i)
        day = time.strftime('%Y.%m.%d', time.localtime())
        self.history.insert(0, day)
        sb3 = Scrollbar(f21)
        sb3.grid(row=1,sticky=N + W*self.system + S + E)
        self.history.configure(yscrollcommand=sb3.set)
        sb3.configure(command=self.history.yview)

        if self.teen_manager.mode:
            self.history['height'] = 5
            f22 = Frame(f2)
            f22.pack()
            Label(f22,text='小組分數',font=_font(20)).grid(row=0)
            self.teenlist = Listbox(f22,listvariable=self.teen,width=10,height=9,font=_font(20))
            self.teenlist.grid(row=1)
            sb2 = Scrollbar(f22)
            sb2.grid(row=1, sticky=N + W*self.system + S + E)
            self.teenlist.configure(yscrollcommand=sb2.set)
            sb2.configure(command=self.teenlist.yview)

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
        self.button=['1','2','3','4','5','6','7','8','9','C','0','回復','扣分','加分']
        for i in range(14):
            Button(f32,text=self.button[i],width=4,height=1,font=_font(30),command=lambda x=i:self.button_up(x)).grid(row=i//3,column=i%3,padx=9,pady=10)
        self.setlist()
    def button_up(self,n=-1):
        b = self.button[n]
        if b == 'C':
            self.entry.delete(0,'end')
        elif b == '回復':
            data = self.history.get(0)
            m,x = data[-1],data[0:-1]
            if m == '+':
                m = -1
            elif m == '-':
                m = 1
            self.data.update(x,m)
            self.setlist()
            self.scorelist.see(int(x)-1)
            self.history.delete(0)
            
        elif b == '加分' or b == '扣分':
            n = self.entry.get()
            if b == '加分':
                self.data.update(n)
                self.history.insert(0,n+'+')
            else:
                self.data.update(n,-1)
                self.history.insert(0,n+'-')
            self.setlist()
            self.entry.delete(0,'end')
            self.scorelist.see(int(n)-1)
            self.data.save()
            self.history_manager.write(self.history.get(0, END))
            
        else:
            self.entry.insert('end',b)
        self.data.save()
l = login.login()
l.wait_login()
if l.start:
    window = mywindow()
    window.mainloop()