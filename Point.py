from math import *

#   y
#   ^
#   |   
#   + - > x
#  /
# z

class Point():

    def __init__(self, x, y, z, **kwargs):
        super(Point, self).__init__(**kwargs)
        self.x, self.y, self.z = x, y, z

    def rotate_x(self, angle, x0, y0, z0):
        r = radians(angle)
        x = x0 + (self.x - x0) * cos(r) - (self.z - z0) * sin(r)
        y = self.y
        z = z0 + (self.x - x0) * sin(r) + (self.z - z0) * cos(r)
        self.x, self.y, self.z = x, y, z
        

    def rotate_y(self, angle, x0, y0, z0):
        r = radians(angle)
        x = x0 + (self.x - x0) * cos(r) - (self.y - y0) * sin(r)
        y = y0 + (self.x - x0) * sin(r) + (self.y - y0) * cos(r)
        z = self.z
        self.x, self.y, self.z = x, y, z
    
    def rotate_z(self, angle, x0, y0, z0):
        r = radians(angle)
        x = self.x
        y = y0 + (self.y - y0) * cos(r) - (self.z - z0) * sin(r)
        z = z0 + (self.y - y0) * sin(r) + (self.z - z0) * cos(r)
        self.x, self.y, self.z = x, y, z

    def pos(self):
        return self.x, self.y, self.z

    