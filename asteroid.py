import uuid

class Asteroid:
    character = 'Q'
    color = "lightsalmon4"

    def __init__(self, position):
        self.position = position
        # Assign a unique name using UUID to avoid name conflicts
        self.name = f"asteroid-{uuid.uuid4()}"

    def play_turn(self, game):
        if game.turn_number % 2 == 0: 
            x, y = self.position
            if y == game.board_size[1] - 1:
                game.remove_agent_by_name(self.name)
            else:
                ship = game.get_agent_by_name('ship')
                new_position = (x, y + 1)
                if new_position == ship.position:
                    game.end()
                else:
                    self.position = new_position
