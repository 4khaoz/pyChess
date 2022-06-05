"""
Represents the Chess Board on the server
"""

from position import Position

class Board(object):
    ROWS = COLS = 8

    def __init__(self):
        self.data = self.generate_empty_board()

    def generate_empty_board():
        return [[Position(x, y) for x in range(Board.COLS)] for y in range(Board.ROWS)]

    def update_position(self, x, y, piece):
        """
        @param  x       X-Position
        @param  y       Y-Position
        @param  piece   Piece to place on position
        """
        self.data[y][x].piece = piece
