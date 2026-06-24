n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Info():
    def __init__(self, name, street, region):
        self.name = name
        self.street = street
        self.region = region

obj = [
    Info(name[i], street_address[i], region[i]) for i in range(n)
]

obj.sort(key = lambda x:x.name, reverse=True)

print(f'name {obj[0].name}')
print(f'addr {obj[0].street}')
print(f'city {obj[0].region}')
