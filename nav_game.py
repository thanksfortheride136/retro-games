"""from retro.game import Game
from spaceship import Spaceship
from asteroid import Asteroid

board_size = (25, 25)  # Defines the size of the game board
ship = Spaceship(board_size)
asteroid = Asteroid((board_size[0] // 2, 0))  # Use board_size[0] for WIDTH
game = Game([ship, asteroid], {"score": 0}, board_size=board_size)
game.play()"""

from retro.game import Game
from spaceship import Spaceship
from asteroid_spawner import AsteroidSpawner

board_size = (85, 35)
ship = Spaceship(board_size)  # Spaceship uses board_size for initial positioning
spawner = AsteroidSpawner(board_size)  # Spawner uses board_size to spawn asteroids
game = Game([ship, spawner], {"score": 0}, board_size=board_size)  # Game handles entities within board_size
game.play()

