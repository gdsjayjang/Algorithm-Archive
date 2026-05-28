time = input()
hour, min = time.split(':')

hour = int(hour)
min = int(min)

print(f'{hour+1}:{min}')