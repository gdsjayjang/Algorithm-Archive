user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Game:
    def __init__(self, id='codetree', level=10):
        self.id = id
        self.level = level

game1 = Game()
game2 = Game(user2_id, user2_level)

print(f'user {game1.id} lv {game1.level}')
print(f'user {game2.id} lv {game2.level}')