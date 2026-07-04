n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
# check
possible_answers = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue

            target = [i, j, k]

            is_match_all = True

            for q_idx in range(n):
                q_num = a[q_idx]
                q_cnt1 = b[q_idx]
                q_num_str = str(q_num)

                query = [int(q_num_str[0]), int(q_num_str[1]), int(q_num_str[2])]

                current_cnt1 = 0
                current_cnt2 = 0
                
                for pos in range(3):
                    if query[pos] == target[pos]:
                        current_cnt1 += 1
                    elif query[pos] in target:
                        current_cnt2 += 1

                if current_cnt1 != b[q_idx] or current_cnt2 != c[q_idx]:
                    is_match_all = False
                    break

            if is_match_all:
                possible_answers += 1

print(possible_answers)