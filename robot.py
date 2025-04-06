import numpy as np

class Robot:
    def __init__(self, x, y, speed):
        self.position = np.array([x, y], dtype=float)
        self.direction = np.random.uniform(0, 2 * np.pi)  # random initial direction
        self.speed = speed

    #move robot one step forward 
    def move_forward(self):
        dx = self.speed * np.cos(self.direction)
        dy = self.speed * np.sin(self.direction)
        self.position += np.array([dx, dy])

    
    #rotate robot randomly by an angle between -90 deg and +90 deg
    def rotate_randomly(self):
        random_angle = np.random.uniform(-np.pi / 2, np.pi / 2)  # turn by -90 to +90 degrees
        self.direction += random_angle
