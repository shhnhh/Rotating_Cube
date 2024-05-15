import sys
sys.path.insert(0, '../')

from Square import Square  

from kivy.uix.floatlayout import FloatLayout
from math import *
from kivy.clock import Clock

dict_colors = {
    'G': (0, 153 / 255, 0),
    'O': (1, 128 / 255, 0),
    'B': (0, 0, 204 / 255),
    'R': (204 / 255, 0, 0),
    'W': (1, 1, 1),
    'Y': (1, 1, 0)
}

class Cube(FloatLayout):
    
    size_hint = (None, None)
    lst = []

    def __init__(self, colors, side = 100, border = 0, **kwargs):
        super(Cube, self).__init__(**kwargs)

        colors = colors.upper()

        print(len(colors), set(colors) - set('RGBOWY-'))
        if len(colors) != 6 or len(set(colors) - set('RGBOWY-')) > 0:
            raise ValueError

        pos = self.pos
        self.side = side
        self.cx = pos[0] + side / 2
        self.cy = pos[1] + side / 2
        self.cz = side / 2

        angles = ['x0', 'x90', 'x180', 'x270', 'z90', 'z270']

        for i in range(6):
            if colors[i] != '-':
                sqr = Square(pos = pos, side = side, border = border, color = dict_colors[colors[i]])
                sqr.rotate(self.cx, self.cy, self.cz, angles[i])
                self.lst.append(sqr)

        self.reprint()

    def center(self):
        return self.cx, self.cy, self.cz

    def reprint(self):
        self.lst.sort(key = lambda x: x.cz(), reverse = True)

        self.clear_widgets()
        for i in self.lst:
            self.add_widget(i)

    def rotate(self, *angles):
        def foo(dt):
            for j in self.lst:
                j.rotate(self.cx, self.cy, self.cz, *angles)
            self.reprint()

        Clock.schedule_interval(foo, 0.03)


   
