import random
from retro.game import Game

class Player:
    character = "$"
    position = (5, 5)
    color = "red"

    #moves character left / right
    def handle_keystroke(self, keystroke, game):
        x, y = self.position
        if keystroke.name in ("KEY_LEFT", "KEY_RIGHT"):
            if keystroke.name == "KEY_LEFT": 
                new_position = (x - 1, y)
            else: 
                new_position = (x + 1, y)
            if game.on_board(new_position):
                if game.is_empty(new_position):
                    self.position = new_position
                else:
                    game.end()

#enemy
class Enemy:
    character = "E"
    color = "blue"

    def __init__(self, board_size):
        self.board_size = board_size
        self.spawn()

    def spawn(self):
        x = random.randint(0, self.board_size[0] - 1)
        y = random.randint(0, self.board_size[1] - 1)
        self.position = (x, y)

    def move(self, game):
        x, y = self.position
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_position = (x + dx, y + dy)
            if game.on_board(new_position) and game.is_empty(new_position):
                self.position = new_position
                break

player1 = Player()
board_size = (85, 35)
enemy1 = Enemy(board_size)
game = Game([player1, enemy1], {}, board_size)
game.play()