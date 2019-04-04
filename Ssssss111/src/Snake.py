import pygame

from src.Config import*

class Snake:
    def __init__(self, display):
        self.x_pos = (WIDTH -30) / 2
        self.y_pos = (HEIGHT - 30) / 2
        self.display = display
        # self.body = []
        # self.max_size = 0

    # def eat(self):
    #     self.max_size += 1

    def draw(self):
        return pygame.draw.rect(
            self.display, 
            YELLOW,
            [
                self.x_pos,
                self.y_pos,
                SNAKE_HEIGHT,
                SNAKE_WIDTH
            ]
        )

    # def draw_body(self):
    #     for item in self.body:
    #         pygame.draw.rect(
    #             self.display, 
    #             YELLOW,
    #             [
    #                 item[0],
    #                 item[1],
    #                 SNAKE_WIDTH,
    #                 SNAKE_HEIGHT
    #             ]
    #         )

    def move(self, x_change, y_change):
        # self.body.append((self.x_pos, self.y_pos))
        self.x_pos += x_change
        self.y_pos += y_change

        # if len(self.body) > self.max_size:
        #     del(self.body[0])
