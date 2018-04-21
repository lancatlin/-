import tkinter as tk
import tkinter.messagebox
import os

class MainSetter(tk.Toplevel):
    def __init__(self, root, path):
        super().__init__(root)
        self.path = path

        self.title(path + "設定")
        bFrame = tk.Frame(self)
        bFrame.grid(padx=20, pady=30)
        tk.Button(bFrame, text='新分數表', command=self.newScore).grid(row=0, column=0, padx=10)
        tk.Button(bFrame, text='輸出分數表').grid(row=0, column=1, padx=10)
        tk.Button(bFrame, text='建立組員名單').grid(row=0, column=2, padx=10)
        tk.Button(bFrame, text='更改密碼').grid(row=0, column=3, padx=10)

        if path not in os.listdir():
            isCreat = tk.messagebox.askquestion(title='找不到資料夾', message='找不到指定班級，是否創建？')
            if isCreat:
                os.mkdir(path)
            else:
                self.withdraw()

    def newScore(self):
        top = NewScore(self)
        self.wait_window(top)

    def newTeam(self):
        pass

    def outScore(self):
        pass

class NewScore(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('建立新分數表')
        f1 = tk.Frame(self)
        f1.grid(row=0, padx=10, pady=10)
        tk.Label(f1, text='輸入班級人數：').grid(row=0, column=0)
        entry = tk.Entry(f1, width=5)
        entry.grid(row=0, column=1, padx=10)
        f2 = tk.Frame(self)
        f2.grid(row=1, padx=10, pady=10)
        tk.Button(f2, text='確定', command=lambda: self.creat(root.path, entry)).grid(row=0, column=0)
        tk.Button(f2, text='取消', command=lambda: self.withdraw()).grid(row=0, column=1, padx=10)

    def creat(self, path, entry):
        if 'score.sc' in os.listdir(path):
            isCreat = tk.messagebox.askquestion(title='將覆蓋檔案', message='是否要覆蓋現有檔案？')
        else:
            isCreat = True

        if isCreat:
            with open(path + '/score.sc', 'w') as file:
                result = ''
                info = int(entry.get())
                for i in range(1, info+1):
                    result += '%s:0\n' % i
                file.write(result)

        self.withdraw()
            

