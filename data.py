

class Data:
    def __init__(self, path):
        self.path = path
        self.score = {}
        self.team = {}
        self.history = []
        with open(path+'/score.sc', 'r') as file:
            for i in file.read().split('\n'):
                if ':' not in i:
                    break
                name, score = i.split(':')
                self.score[int(name)] = int(score)
        try:
            with open(path+'/team.sc', 'r') as file:
                for i in file.read().split('\n'):
                    if ':' not in i:
                        break
                    name, people = i.split(':')
                    self.team[int(name)] = [int(p) for p in people.split(',')]
        except FileNotFoundError:
            self.team = None
        try:
            with open(path+'/history.sc', 'r') as file:
                self.history = [h for h in file.read().split('\n')]
        except FileNotFoundError:
            with open(path+'/history.sc', 'w') as file:
                self.history = []

    def update(self, name, plus, history=None):
        self.score[name] += plus
        if history:
            self.history = history
    
    def get(self, mode=False):
        score = []
        for key in sorted(self.score):
            score.append('%s:%s' % (key, self.score[key]) if mode \
                    else '%s號: %s' % (key, self.score[key]))
        team_score = []
        if not mode:
            for key in sorted(self.team):
                team_score.append('%s組(%s): %s' % (key, self.team[key][0], sum(self.team[key])))
        
        return score, team_score

    def write(self):
        score, t = self.get(True)
        with open(self.path+'/score.sc', 'w') as file:
            file.write('\n'.join(score))
        
        with open(self.path+'/history.sc', 'w') as file:
            file.write('\n'.join(self.history))

