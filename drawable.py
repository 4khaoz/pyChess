"""
Drawable Interface
"""

from pygame import Surface, Color, Rect, draw, transform

class IDrawable:
    WHITE_FIELD = Color((255, 255, 255))
    BLACK_FIELD = Color((100, 100, 100))

    def render(self, screen: Surface):
        pass