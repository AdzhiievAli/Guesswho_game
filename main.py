import pygame
from main_menu import MainMenu

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Guess Who")
    main_menu = MainMenu(screen)
    main_menu.run()
