str = input()

str = list(str)
str.pop(2)
str.pop(-2)
print(*str, sep='')