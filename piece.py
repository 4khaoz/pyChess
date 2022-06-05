"""
Represents a chess piece
"""

import os
from drawable import *
from pygame import image

class Piece(IDrawable, object):
    def __init__(self, filename):
        self.img = transform.scale(image.load(os.path.join("assets", filename)), (100, 100))

    def render(self, screen: Surface, dest: Rect):
        screen.blit(self.img, dest)