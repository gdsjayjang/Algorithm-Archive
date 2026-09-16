n = int(input())
inp = map(int, input().split())

arr = [i**2 for i in inp]
print(*arr, sep=' ')