time = input()
hour, min = time.split(':')

hour = int(hour)
min = int(min)

print(hour+1, min, sep=':')