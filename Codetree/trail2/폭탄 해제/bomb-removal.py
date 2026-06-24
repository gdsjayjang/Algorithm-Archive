unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb():
    def __init__ (self, code, color, seconds):
        self.code = code
        self.color = color
        self.seconds = seconds

obj = Bomb(unlock_code, wire_color, seconds)

print(f'code : {obj.code}')
print(f'color : {obj.color}')
print(f'second : {obj.seconds}')
