from random import randint
from asteroid import Asteroid

class AsteroidSpawner:
    display = False

    def __init__(self, board_size):
        width, height = board_size
        self.board_width = width

    def play_turn(self, game):
        game.state['score'] += 1
        if self.should_spawn_asteroid(game.turn_number):
            asteroid = Asteroid((randint(0, self.board_width - 1), 0))
            game.add_agent(asteroid)

    def should_spawn_asteroid(self, turn_number):
        return randint(0, 1000) < turn_number