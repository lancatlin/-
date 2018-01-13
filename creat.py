    #creat_new window
import sys
import login
import os


class setting:
    def __init__(self):
        self.path = input('輸入班級：')
        if self.path not in os.listdir():
            print('班級不存在')
            input('按enter結束程式')
        else:
            self.path += '/'
            mode = input('模式:(1)建立新分數表 (2)建立組員名單 (3)更改密碼:')
            if mode == '1':
                self.creat()
            elif mode == '2':
                self.new_teen()
            elif mode == '3':
                self.new_code()
    def creat(self):
        print('即將新增新的分數表，取消請輸入exit')
        name = input('輸入舊分數表名稱(如不要請留空): ')
        if name == 'exit':
            sys.exit()
        elif name != '':
            with open(self.path+'score.sc', 'r') as file:
                with open(name, 'w') as new:
                    new.write(file.read())
        print('-'*50)
        print('新分數表設定:')
        while True:
            info = input('新分數表長度: ')
            try:
                info = int(info)
                break
            except:
                if info == 'exit':
                    sys.exit()
                print('請輸入數字')
        with open(self.path+'score.sc', 'w') as file:
            result = ''
            for i in range(1, info+1):
                result += str(i)+':0\n'
            file.write(result)
        input('新分數表已建立完成，請重新啟動加分程式')
    def new_teen(self):
        print('即將新增新的組員表，取消請輸入exit')
        name = input('輸入舊組員表名稱(如不要請留空): ')
        if name == 'exit':
            sys.exit()
        elif name != '':
            with open(self.path+'teen.sc', 'r') as file:
                with open(name, 'w') as new:
                    new.write(file.read())
        print('-' * 50)
        print('新組員表設定:')
        result = []
        num = 0
        again = True
        while again:
            result.append([])
            p = 1
            while True:
                info = input('第{0}組 第{1}位: '.format(num+1,p))
                if info == 'exit':
                    again = False
                    break
                elif info == '':
                    break
                else:
                    result[num].append(info)
                    p += 1
            num += 1
        print(result)
        with open(self.path+'teen.sc', 'w') as file:
            string = ''
            for i in range(len(result)):
                string += str(i+1)+':'+(','.join(result[i]))+'\n'
            print(string)
            file.write(string)
        input('新組員表已建立完成，請重新啟動加分程式')
    def new_code(self):
        x = 10
        print('即將改變密碼，取消請輸入exit')
        try:
            f = open(self.path+'code.sc','r')
            code = f.read()
            while code != '':
                name = input('輸入舊密碼: ')
                if name == 'exit':
                    sys.exit()
                elif name == login.encode(code,x):
                    break
                else:
                    print('密碼錯誤')
        except IOError:
            pass
        print('-' * 50)
        print('新密碼設定:')
        while True:
            try:
                info = input('輸入新密碼: ')
                if info == 'exit':
                    sys.exit()
                break
            except:
                print('請輸入數字')
        with open(self.path+'code.sc', 'w') as file:
            result = login.encode(info,-x)
            file.write(result)
        input('新密碼已建立完成，請重新啟動加分程式')


setting()