str1, str2 = input().split()

len1 = len(str1)
len2 = len(str2)

if len1 == len2:
    print('same')
elif len1 > len2:
    print(str1, len1)
else:
    print(str2, len2)