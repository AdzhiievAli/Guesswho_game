import pygame
from main_logic import GuessWhoGame
from select_pack import select_pack

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))  
    pygame.display.set_caption('Guess Who')

    pack = select_pack(screen)
    game = GuessWhoGame(screen, pack)
    game.run()
