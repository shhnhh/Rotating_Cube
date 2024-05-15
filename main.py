from kivy.app import *
from kivy.uix.floatlayout import FloatLayout
from time import *
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import sys
sys.path.insert(0, '../')

from Square import Square
from Cube import Cube

class MyApp(App):

    def build(self):
        cube = Cube('RGBOWY', pos = (200, 200), side = 250, border = 5)
        cube.rotate('x10', 'z10')
        return cube

if __name__ == '__main__':
    MyApp().run()