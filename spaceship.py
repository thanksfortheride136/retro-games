class Spaceship:
    name = "ship"
    character = '^'
    color = 'red'

    def __init__(self, board_size):
        board_width, board_height = board_size
        self.position = (board_width // 2, board_height - 1)

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