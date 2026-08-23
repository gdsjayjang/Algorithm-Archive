secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Agent:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

agent1 = Agent(secret_code, meeting_point, time)

print('secret code :', agent1.code)
print('meeting point :', agent1.point)
print('time :', agent1.time)