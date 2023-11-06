import math
import pygame

#Anything white is considered out of boudns
BORDER_COLOR = (255, 255, 255, 255)
CAR_SIZE_X = 60    
CAR_SIZE_Y = 60


class Car:
    def __init__(self):
        self.speed =0
        self.isalive = True
        self.position = [100,100]
        self.angle = 0
        self.radars = []
        self.time = 0
        self.distance = 0


        self.center = [self.position[0] + CAR_SIZE_X / 2, self.position[1] + CAR_SIZE_Y / 2] # Calculate Center
        # Calculate Four Corners
        # Length Is Half The Side
        length = 0.5 * CAR_SIZE_X
        left_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * length]
        right_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * length]
        left_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * length]
        right_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * length]
        self.corners = [left_top, right_top, left_bottom, right_bottom]

    # Checks if any corner of the car has went out of bounds, aka touched white
    def crash(self, track):
        self.alive = True
        for point in self.corners:
            if  track.get_at(point[0], point[1])==BORDER_COLOR:
                self.alive = False
                break



    def run_simulation():
        pygame.init()
        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)