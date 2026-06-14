n = int(input())

cnt = 1
cnt_class = 0
cnt_bok = 0
cnt_toilet = 0

for _ in range(n):
    if cnt % 12 == 0:
        cnt_toilet += 1
    elif cnt % 3 == 0:
        cnt_bok += 1
    elif cnt % 2 == 0:
        cnt_class += 1
    cnt += 1

print(cnt_class, cnt_bok, cnt_toilet)