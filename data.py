class score_manager:
    def __init__(self):
        with open('score.sc','r') as file:
            score = file.readlines()
            print(score)
        self.data = []
        for i in score:
            n,s = i.split(':')
            s = int(s)
            self.data.append(score_data(n,s))
    def update(self,n,plus=1):
        for i in self.data:
            i.update(n,plus)
    def get(self,mode=False):
        result = []
        for i in self.data:
            result.append(i.get(mode))
        return result
    def save(self):
        result='\n'.join(self.get(True))
        with open('score.sc','w') as file:
            file.write(result)
class score_data:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def update(self,n,plus):
        if n == self.name:
            self.score += plus
    def get(self,save=False):
        if save:
            return self.name+':'+str(self.score)
        else:
            return self.name+'號: '+str(self.score)