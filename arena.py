class Arena:
    def __init__(self, size):
        self.size = size  

    #Detect if the robot has hit any arena boundaries.
    def check_collision(self, robot):
        x, y = robot.position

        #Check if position is at or outside any of the four walls
        if x <= 0 or x >= self.size or y <= 0 or y >= self.size:
            return True
        return False
