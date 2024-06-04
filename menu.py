import pygame
import os


class Menu:
    def __init__(self, screen, buttons, title=None, show_game_title=False, title_y=120):
        self.screen = screen
        self.buttons = buttons
        self.title = title
        self.font = pygame.font.Font(None, 48)
        self.game_title_font = pygame.font.Font(None, 75)
        self.show_game_title = show_game_title
        self.title_y = title_y  
        self.background_image = "background.jpg"
        if os.path.exists(self.background_image):
            self.background = pygame.image.load(self.background_image)
        else:
            self.background = None

    def draw(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill((135, 206, 250))

        if self.show_game_title:
            game_title_surface = self.game_title_font.render("GuessWho", True, (255, 255, 255))
            self.screen.blit(game_title_surface, (400 - game_title_surface.get_width() // 2, 80))

        if self.title:
            title_surface = self.font.render(self.title, True, (255, 255, 255))
            self.screen.blit(title_surface, (400 - title_surface.get_width() // 2, self.title_y))
        
        for button in self.buttons:
            button.draw(self.screen)