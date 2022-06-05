"""
Represents a chess piece
"""

import os
from pygame import image

class Piece(object):
    def __init__(self, filename):
        self.img = image.load(os.path.join("assets", filename))