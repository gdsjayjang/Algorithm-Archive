m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start = sum(months[:m1-1]) + d1-1
end = sum(months[:m2-1]) + d2

print(end-start)