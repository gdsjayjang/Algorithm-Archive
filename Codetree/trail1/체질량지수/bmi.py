inp = input()
arr = inp.split()

height = int(arr[0])
weight = int(arr[1])

bmi = 10000 * weight // height**2

print(bmi)
if bmi >= 25:
    print('Obesity')