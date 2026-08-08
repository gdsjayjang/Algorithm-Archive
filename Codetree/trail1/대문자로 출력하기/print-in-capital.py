arr = list(input())

for i in arr:
    if i.isalpha():
        print(i.upper(), end='')