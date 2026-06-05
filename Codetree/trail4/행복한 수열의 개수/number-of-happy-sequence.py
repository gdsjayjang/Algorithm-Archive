n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
if m == 1:
    print(2 * n)
else:
    cnt_list_raw = []
    for i in range(n):
        cnt = 1
        max_cnt = 1
        for j in range(n-1):

            if grid[i][j] == grid[i][j+1]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        cnt_list_raw.append(max_cnt)

    # 열 먼저
    cnt_list_col = []
    for j in range(n):
        cnt = 1
        max_cnt = 1
        for i in range(n-1):

            if grid[i][j] == grid[i+1][j]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        cnt_list_col.append(max_cnt)


    res = 0
    for i in range(n):
        if cnt_list_raw[i] >= m:
            res += 1

    for i in range(n):
        if cnt_list_col[i] >= m:
            res += 1

    print(res)