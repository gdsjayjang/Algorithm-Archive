n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
new_li = sorted(nums)
print(new_li[k-1])