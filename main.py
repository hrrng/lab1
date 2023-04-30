from figures import Figure
import Circle
import Triangle
import Square
import Polygon
import Line
import Ellipse
import Reader
import pygame as pyg

pyg.init()
size = (800, 800)
screen = pyg.display.set_mode(size)
pyg.display.set_caption("Лаба1")
clock = pyg.time.Clock()


if __name__ == '__main__':
    info = Reader.read_file('figures.json')

    figures = []
    for item in info['figures']:
        if item['type'] == 'circle':
            figures.append(Circle(item['center_x'],
                              item['center_y'],
                              item['radius'],
                              item['line_color'],
                              item['bg_color'],
                              item['depth']))
        elif item['type'] == 'triangle':
            figures.append(Triangle(item['x1'],
                              item['y1'],
                              item['x2'],
                              item['y2'],
                              item['x3'],
                              item['y3'],
                              item['line_color'],
                              item['bg_color'],
                              item['depth']))
        elif item['type'] == 'square':
            figures.append(Square(item['x'],
                              item['y'],
                              item['size'],
                              item['line_color'],
                              item['bg_color'],
                              item['depth']))
        elif item['type'] == 'polygon':
            figures.append(Polygon(item['x'],
                              item['y'],
                              item['size'],
                              item['line_color'],
                              item['bg_color'],
                              item['depth']))
        elif item['type'] == 'line':
            figures.append(Line(item['x1'],
                                item['y1'],
                                item['x2'],
                                item['y2'], item['line_color'],
                                item['depth']))
        elif item['type'] == 'ellipse':
            figures.append(Ellipse(figures.append(Circle(item['center_x'],
                              item['center_y'],
                              item['width'],
                              item['height'],
                              item['line_color'],
                              item['bg_color'],
                              item['depth']))))
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.QUIT()
                quit()
        screen.fill(300, 300, 300)
        for figure in figures:
            figure.draw(screen)
        pyg.display.update()