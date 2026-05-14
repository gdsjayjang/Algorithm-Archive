char = input()
str_list = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0

for i in str_list:
    if (i[2] == char) or (i[3] == char):
        print(i)
        cnt += 1
print(cnt)