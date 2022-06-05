"""
Represents the Chess Board on the server
"""

from piece import Piece
from position import Position
from drawable import *

class Board(IDrawable, object):
    ROWS = COLS = 8
    FIELD_SIZE = 100
    FIELD_COLORS = [IDrawable.WHITE_FIELD, IDrawable.BLACK_FIELD]

    def __init__(self):
        self.pos_data = self.generate_empty_board()

        # Test
        self.pos_data[0][4].piece = Piece("black_king.png")

    def generate_empty_board(self):
        """
        Creates a 2D-Array of Positions without chess pieces
        """
        return [
            [Position(x, y, self.FIELD_SIZE, Color(self.FIELD_COLORS[(x+y)%2])) for x in range(Board.COLS)] 
            for y in range(Board.ROWS)
        ]

    def update_position(self, x, y, piece: Piece):
        """
        @param  x       X-Position
        @param  y       Y-Position
        @param  piece   Piece to place on position
        """
        self.data[y][x].piece = piece

    def render(self, screen: Surface):
        """
        Draw each chess field
        """
        draw.rect(screen, Color('white'), Rect(0, 0, 800, 800))
        for y in range(self.ROWS):
            for x in range(self.COLS):
                self.pos_data[y][x].render(screen)

