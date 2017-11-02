    #creat_new window
import sys
def creat():
    print('即將新增新的分數表，取消請輸入exit')
    name = input('輸入舊分數表名稱(如不要請留空): ')
    if name == 'exit':
        sys.exit()
    elif name != '':
        with open('score.sc','r') as file:
            with open(name,'w') as new:
                new.write(file.read())
    print('-'*50)
    print('新分數表設定:')
    while True:
        try:
            info = int(input('新分數表長度: '))
            break
        except:
            if info == 'exit':
                sys.exit()
            print('請輸入數字')
    with open('score.sc','w') as file:
        result = ''
        for i in range(1,info+1):
            result+=str(i)+':0\n'
        file.write(result)
    input('新分數表已建立完成，請重新啟動加分程式')
if __name__ == '__main__':
    creat()