import pygame as pyg
from figures import Figure

class Triangle(Figure):
    def __init__(self, x1, y1,x2, y2, x3, y3, radius, line_color, bg_color, depth):
        super().__init__(line_color, bg_color, depth)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self, screen):
        points = [(self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)]
        if self.bg_color:
            pyg.draw.polygon(screen, self.bg_color, points)
            pyg.draw.polygon(screen, self.line_color, points, self.depth)