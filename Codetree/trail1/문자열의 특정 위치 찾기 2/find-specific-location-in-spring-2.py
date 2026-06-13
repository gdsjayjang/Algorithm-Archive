char = input()
li = ['apple', 'banana', 'grape', 'blueberry', 'orange']

cnt = 0
for i in li:
    if (char == i[2]) or (char == i[3]):
        cnt +=1
        print(i)

print(cnt)