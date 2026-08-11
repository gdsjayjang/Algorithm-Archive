inp = list(input())

for i in inp:
    if i == 'e':
        inp.remove(i)
        break

print(*inp, sep='')