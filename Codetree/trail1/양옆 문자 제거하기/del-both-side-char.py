str = input()

str = list(str)
str.pop(1)
str.pop(-2)
print(*str, sep='')