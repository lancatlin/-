import os


class score_manager:
    def __init__(self):
        with open('score.sc','r') as file:
            score = file.readlines()
        self.data = []
        for i in score:
            n,s = i.split(':')
            s = int(s)
            self.data.append({'name':n,'score':s})

    def update(self,n,plus=1):
        for i in self.data:
            if i['name'] == n:
                i['score']+=plus

    def get(self,mode=False,p=0):
        result = []
        if p == 0:
            for i in self.data:
                if mode:
                    result.append(i['name'] + ':' + str(i['score']))
                else:
                    result.append(i['name'] + '號: ' + str(i['score']))
            return result
        else:
            return self.data[p-1]['score']

    def save(self):
        result='\n'.join(self.get(True))
        with open('score.sc','w') as file:
            file.write(result)


class teen:
    def __init__(self,manager):
        self.manager = manager
        self.mode = True
        try:
            file = open('teen.sc','r')
            t = file.readlines()
            self.data = []
            for i in t:
                i = i[0:-1]
                n, a = i.split(':')
                p = []
                for x in a.split(','):
                    p.append(int(x))
                self.data.append({'name': n, 'people': p, 'score': 0})
            print(self.data)
        except IOError:
            self.mode = False

    def update(self):
        for i in self.data:
            i['score'] = 0
            for j in i['people']:
                i['score'] += self.manager.get(False,j)
        return self.data

    def get(self):
        self.update()
        result = []
        for i in self.data:
            result.append('%s組(%s): %s' % (i['name'], i['people'][0], i['score']))
        return result


class history:
    def read(self):
        try:
            with open('history.sc', 'r') as file:
                data = file.read().split('\n')
                print(data)
                return data
        except FileNotFoundError:
            with open('history.sc', 'w') as file:
                return []

    def write(self, data):
        with open('history.sc', 'w') as file:
            if len(data) > 50:
                result = '\n'.join(data[0:50])
            else:
                result = '\n'.join(data)
            file.write(result)


if __name__ == '__main__':
    teen(score_manager())