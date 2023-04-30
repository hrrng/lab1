import pygame as pyg
from figures import Figure


class Ellipse(Figure):
    def __init__(self, center_x, center_y, major_axis, minor_axis, line_color, bg_color, depth):
        super().__init__(line_color, bg_color, depth)
        self.center_x = center_x
        self.center_y = center_y
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def draw(self, screen):
        ellps = pyg.Rect(self.center_x - self.major_axis,
                         self.center_y - self.minor_axis,
                         2*self.major_axis,
                         2*self.minor_axis)
        pyg.draw.ellipse(screen, self.bg_color, ellps)
        pyg.draw.ellipse(screen, self.line_color, ellps, self.depth)