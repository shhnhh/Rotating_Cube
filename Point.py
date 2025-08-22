import numpy as np

#   y
#   ^
#   |   
#   + - > x
#  /
# z

class Point:

    def __init__(self, x, y, z, **kwargs):
        super(Point, self).__init__(**kwargs)
        self.coords = np.array([x, y, z], dtype=np.float32)

    def rotate_x(self, angle, x0, y0, z0):
        r = np.radians(angle)
        rot_matrix = np.array([
            [np.cos(r), 0, np.sin(r)],
            [0, 1, 0],
            [-np.sin(r), 0, np.cos(r)]
        ])
        self.coords -= (x0, y0, z0)
        self.coords = rot_matrix @ self.coords
        self.coords += (x0, y0, z0)

    def rotate_y(self, angle, x0, y0, z0):
        r = np.radians(angle)
        rot_matrix = np.array([
            [np.cos(r), -np.sin(r), 0],
            [np.sin(r), np.cos(r), 0],
            [0, 0, 1]
        ])
        self.coords -= (x0, y0, z0)
        self.coords = rot_matrix @ self.coords
        self.coords += (x0, y0, z0)
    
    def rotate_z(self, angle, x0, y0, z0):
        r = np.radians(angle)
        rot_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(r), -np.sin(r)],
            [0, np.sin(r), np.cos(r)]
        ])
        self.coords -= (x0, y0, z0)
        self.coords = rot_matrix @ self.coords
        self.coords += (x0, y0, z0)

    def pos(self):
        return self.coords
    

    