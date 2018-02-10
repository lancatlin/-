import os


class ScoreManager:
    def __init__(self, room):
        self.path = room+'/score.sc'
        with open(self.path, 'r') as file:
            score = file.readlines()
        self.data = {}
        for i in score:
            n,s = i.split(':')
            self.data[int(n)] = int(s)

    def update(self,n,plus=1):
        self.data[n] += plus

    def get(self,mode=False,p=0):
        if p == 0:
            result = []
            for key in sorted(self.data):
                result.append('%s:%s' % (key, self.data[key]) if mode \
                        else '%s號: %s' % (key, self.data[key]))
            return result
        else:
            return self.data[p]

    def save(self):
        result='\n'.join(self.get(True))
        with open(self.path, 'w') as file:
            file.write(result)


class Team:
    def __init__(self, manager, room):
        self.path = room+'/team.sc'
        self.manager = manager
        self.mode = True
        try:
            file = open(self.path, 'r')
            self.data = []
            for i in file.read().split('\n'):
                n, a = i.split(':')
                p = [int(x) for x in a.split(',')]
                self.data.append({'name': n, 'people': p, 'score': 0})
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
    def __init__(self, room):
        self.path = room+'//history.sc'
    def read(self):
        try:
            with open(self.path, 'r') as file:
                data = file.read().split('\n')
                return data
        except FileNotFoundError:
            with open(self.path, 'w') as file:
                return []

    def write(self, data):
        with open(self.path, 'w') as file:
            result = '\n'.join(data[0:50]) if len(data) > 50 \
                    else '\n'.join(data)
            file.write(result)

