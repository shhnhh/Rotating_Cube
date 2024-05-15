import sys
sys.path.insert(0, '../')

from Point import Point  

from kivy.uix.widget import Widget
from kivy.graphics import Quad, Color, Line
from math import *
from itertools import *

class Square(Widget):

    size_hint = (None, None)
    lst = []
    boreder_lst = []

    def __init__(self, side, color, border = 0, **kwargs):
        super(Square, self).__init__(**kwargs)

        pos = self.pos
        self.side = side
        self.color = color

        self.boreder_lst = (
            Point(pos[0], pos[1], 0),
            Point(pos[0], pos[1] + self.side, 0),
            Point(pos[0] + self.side, pos[1] + self.side, 0),
            Point(pos[0] + self.side, pos[1], 0),
        )

        self.lst = (
            Point(pos[0] + border, pos[1] + border, 0),
            Point(pos[0] + border, pos[1] + self.side - border, 0),
            Point(pos[0] + self.side - border, pos[1] + self.side - border, 0),
            Point(pos[0] + self.side - border, pos[1] + border, 0),
        )

        self.reprint()        

    def reprint(self):

        self.canvas.clear()
        with self.canvas:
            Color(0, 0, 0)
            Quad(points = chain.from_iterable(i.pos()[:2] for i in self.boreder_lst))
            Color(*self.color)
            Quad(points = chain.from_iterable(i.pos()[:2] for i in self.lst))

    def rotate_x(self, angle, x0, y0, z0):
        for p in self.boreder_lst:
            p.rotate_x(angle, x0, y0, z0)
        for p in self.lst:
            p.rotate_x(angle, x0, y0, z0)

    def rotate_y(self, angle, x0, y0, z0):
        for p in self.boreder_lst:
            p.rotate_y(angle, x0, y0, z0)
        for p in self.lst:
            p.rotate_y(angle, x0, y0, z0)
    
    def rotate_z(self, angle, x0, y0, z0):
        for p in self.boreder_lst:
            p.rotate_z(angle, x0, y0, z0)
        for p in self.lst:
            p.rotate_z(angle, x0, y0, z0)   

    def rotate(self, x0, y0, z0, *angles):
        for i in angles:
            try:
                c, angle = i[0], int(i[1:])
            except:
                continue
            if c == 'x':
                self.rotate_x(angle, x0, y0, z0)
            elif c == 'y':
                self.rotate_y(angle, x0, y0, z0)
            elif c == 'z':
                self.rotate_z(angle, x0, y0, z0)
        
        self.reprint()

    def cz(self):
        lst_z = [i.pos()[2] for i in self.lst]
        return (min(lst_z) + max(lst_z)) / 2
