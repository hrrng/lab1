import pygame as pyg
from figures import Figure


class Line(Figure):
    def __init__(self, x1, y1, x2, y2, line_color,depth):
        super().__init__(line_color, None, depth)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, screen):
        pyg.draw.line(screen, self.line_color, (self.x1, self.y1), (self.x2, self.y2), self.depth)