n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
dict = {
    'G': 1,
    'H': 2
}
L = 10000
arr = [0] * (L+1)

for elem, str in zip(x, c):
    arr[elem] = dict[str]

res = 0
for i in range(L-k+1):
    sum = 0
    for j in range(i, i+k+1):
        sum += arr[j]
    res = max(res, sum)

print(res)