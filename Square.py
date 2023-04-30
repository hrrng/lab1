import pygame as pyg
from figures import Figure


class Square(Figure):
    def __init__(self, x, y, side, line_color, bg_color, depth):
        super().__init__(line_color, bg_color, depth)
        self.x = x
        self.y = y
        self.side = side

    def draw(self, screen):
        sqr = pyg.Rect(self.x, self.y, self.side, self.side)
        if self.bg_color:
            pyg.draw.rect(screen, self.bg_color, sqr)
            pyg.draw.rect(screen, self.line_color, sqr, self.depth)
