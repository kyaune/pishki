import pygame

from src.Game import Game
from src.Config import*

def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(NAME)

    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()  
