inp1 = input()
arr1 = inp1.split()
inp2 = input()
arr2 = inp2.split()

a1 = int(arr1[0])
a2 = arr1[1]
b1 = int(arr2[0])
b2 = arr2[1]

if (a1 >= 19) and (a2 == 'M'):
    print(1)
elif (b1 >= 19) and (b2 == 'M'):
    print(1)
else:
    print(0)