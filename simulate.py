import matplotlib.pyplot as plt
import numpy as np
import time

from robot import Robot
from arena import Arena

def draw_robot(ax, robot):
    ax.clear()
    ax.set_xlim(0, 10) #arena x boundary
    ax.set_ylim(0, 10) #arema y boundary

    #robot is drawn as a blue circle with radius 0.2
    circle = plt.Circle((robot.position[0], robot.position[1]), 0.2, color='blue')
    ax.add_artist(circle)
    ax.set_title("Brownian Motion Simulation")
    plt.pause(0.01)

def main():
    arena_size = 10
    arena = Arena(arena_size)

    #put robot in the center of the arena
    robot = Robot(arena_size / 2, arena_size / 2, speed=0.05)

    fig, ax = plt.subplots()
    plt.ion()

    for _ in range(1000):  #run for 1000 steps

        #move robot forward
        robot.move_forward()

        #check for collision
        if arena.check_collision(robot):

            #rotate randomly after collision
            robot.rotate_randomly()

            # Reposition if stuck out of bounds
            robot.position = np.clip(robot.position, 0, arena_size)

        draw_robot(ax, robot)

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
