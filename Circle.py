import pygame as pyg
from figures import Figure



class Circle(Figure):
    def __init__(self, center_x, center_y, radius, line_color, bg_color, depth):
        super().__init__(line_color, bg_color, depth)
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def draw(self, screen):
        pyg.draw.circle(screen, self.bg_color,(self.center_x, self.center_y), self.radius)
        pyg.draw.circle(screen, self.line_color, (self.center_x, self.center_y), self.radius, self.depth)

