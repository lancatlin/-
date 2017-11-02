#window
#cmd /k cd C:\Users\Lin\Google 雲端硬碟\python\AddPoints & python "$(FULL_CURRENT_PATH)" &PAUSE&EXIT
from tkinter import *
import data
class mywindow():
    def __init__(self):
        _font = lambda b: ('微軟正黑體',b)
        self.start = lambda: self.window.mainloop()
        self.window = Tk()
        self.window.geometry('800x600')
        #資料
        self.var = StringVar()
        self.data = data.score_manager()
        self.update = lambda :self.var.set(self.data.get())
        
        f1 = Frame(self.window)
        f1.grid(row=1,column=1,padx=15,sticky=N)
        Label(f1,text='分數',font=_font(20)).grid(row=0)
        
        self.update()
        self.scorelist = Listbox(f1,listvariable=self.var,width=10,height=15,font=_font(20))
        self.scorelist.grid(row=1)
        sb = Scrollbar(f1)
        sb.grid(row=1,sticky=N+W+S+E)
        self.scorelist.configure(yscrollcommand=sb.set)
        sb.configure(command=self.scorelist.yview)
        
        f2 = Frame(self.window)
        f2.grid(row=1,column=2,padx=5,sticky=N)
        Label(f2,text='歷史',font=_font(20)).grid(row=0)
        
        self.hlist = Listbox(f2,width=10,height=15,font=_font(20))
        self.hlist.grid(row=1)
        
        f3 = Frame(self.window)
        f3.grid(row=1,column=3,padx=20)
        
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
        
        self.start()
    def button_up(self,n=-1):
        b = self.button[n]
        if b == 'C':
            self.entry.delete(0,'end')
        elif b == '回復':
            data = self.hlist.get(0)
            m,x = data[-1],data[0:-1]
            if m == '+':
                m = -1
            elif m == '-':
                m = 1
            self.data.update(x,m)
            self.update()
            self.scorelist.see(int(x)-1)
            self.hlist.delete(0)
            
        elif b == '加分' or b == '扣分':
            n = self.entry.get()
            if b == '加分':
                self.data.update(n)
                self.hlist.insert(0,n+'+')
            else:
                self.data.update(n,-1)
                self.hlist.insert(0,n+'-')
            self.update()
            self.entry.delete(0,'end')
            self.scorelist.see(int(n)-1)
            self.data.save()
            
        else:
            self.entry.insert('end',b)
        self.data.save()
mywindow()