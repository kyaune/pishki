import random
import pygame

from src.Config import*

class Apple:
    def __init__(self, display):
        self.x_pos = 0
        self.y_pos = 0

        self.display = display

        self.randomize()

    def randomize(self):
        max_x = (HEIGHT - BUMPER_SIZE - SNAKE_WIDTH)
        max_y = (HEIGHT - BUMPER_SIZE - SNAKE_HEIGHT) 
        
        self.x_pos = random.randint(BUMPER_SIZE, max_x)
        self.y_pos = random.randint(BUMPER_SIZE, max_y)

    def draw(self):
        return pygame.draw.rect(
            self.display, 
            YELLOW,
            [
                self.x_pos,
                self.y_pos,
                APPLE_HEIGHT,
                APPLE_WIDTH
            ]
        )