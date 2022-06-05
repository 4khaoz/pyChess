"""
Represents a single position on the Board
e.g. A1, A2, ...
"""

from drawable import *

class Position(object):
    def __init__(self, x: int, y: int, sq_size: int, color: Color):
        """
        @param  x           Board Column
        @param  y           Board Row
        @param  sq_size     Square Size to render
        @param  color       Field Color
        """
        self.x = x
        self.y = y
        self.sq_size = sq_size
        self.location = Rect(x * sq_size, y * sq_size, sq_size, sq_size)
        self.color = color
        self.piece = None
        self.is_hightlighted = False

    def is_occupied(self):
        return self.piece != None

    def get_piece(self):
        return self.piece

    def toggle_highlight(self):
        """
        TODO: Highlight-Border if position is selected/can be moved to
        """
        self.is_hightlighted = not self.is_hightlighted

    def render(self, screen: Surface):
        draw.rect(screen, self.color, self.location)
        if self.piece:
            self.piece.render(screen, self.location)

    def __str__(self):
        # Upper Case A starts at 65
        return f"{chr(self.x + 65)}:{self.y + 1}"