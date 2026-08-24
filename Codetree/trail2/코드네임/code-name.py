MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self, codename='', score=0):
        self.codename = codename
        self.score = score

agents = [Agent(codenames[i], scores[i]) for i in range(MAX_N)]
min_score = min(scores)

for i in range(MAX_N):
    if agents[i].score == min_score:
        print(agents[i].codename, agents[i].score)