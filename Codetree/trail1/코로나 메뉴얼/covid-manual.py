inp1 = input()
arr1 = inp1.split()

inp2 = input()
arr2 = inp2.split()

inp3 = input()
arr3 = inp3.split()

a1 = arr1[0]
a2 = int(arr1[1])

b1 = arr2[0]
b2 = int(arr2[1])

c1 = arr3[0]
c2 = int(arr3[1])

cnt = 0
if (a1 == 'Y') and (a2 >= 37):
    cnt += 1
if (b1 == 'Y') and (b2 >= 37):
    cnt += 1
if (c1 == 'Y') and (c2 >= 37):
    cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')