"""
Represents a single position on the Board
e.g. A1, A2, ...
"""

class Position(object):
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.piece = None

    def get_x_position(self):
        return self.x_pos

    def get_y_position(self):
        return self.y_pos

    def is_occupied(self):
        return self.piece != None

    def get_piece(self):
        return self.piece

    def __str__(self):
        # Upper Case A starts at 65
        return f"{chr(self.x_pos + 65)}:{self.y_pos + 1}"