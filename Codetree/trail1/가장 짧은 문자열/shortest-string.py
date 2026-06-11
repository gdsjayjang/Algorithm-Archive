a = input()
b = input()
c = input()

len_a = len(a)
len_b = len(b)
len_c = len(c)

max_len = max(len_a, len_b, len_c)
min_len = min(len_a, len_b, len_c)

print(max_len - min_len)