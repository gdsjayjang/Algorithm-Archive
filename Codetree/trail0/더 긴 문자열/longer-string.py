str = input().split()

if len(str[0]) > len(str[1]):
    print(str[0], len(str[0]))
elif len(str[0]) < len(str[1]):
    print(str[1], len(str[1]))
else:
    print('same')