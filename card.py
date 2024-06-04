import pygame

class Card:
    def __init__(self, image, name, position):
        self.image = pygame.transform.scale(image, (200, 200))
        self.rect = self.image.get_rect(topleft=position)
        self.name = name
        self.font = pygame.font.SysFont(None, 24)
        self.text = self.font.render(name, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.rect.centerx, self.rect.bottom + 15))
        self.active = True

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

    def click(self, pos):
        if self.active and self.rect.collidepoint(pos):
            self.active = False
            return True
        return False
