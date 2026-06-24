n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class Person():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def __str__(self):
        return f'{self.name} {self.height} {self.weight}'

obj = [
    Person(name[i], height[i], weight[i]) for i in range(5)
]

obj.sort(key = lambda x:(x.name))
print('name')
print(*obj, sep='\n')

print()

obj.sort(key = lambda x:(x.height), reverse=True)
print('height')
print(*obj, sep='\n')
