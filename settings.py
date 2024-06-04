import pygame
import json
import os

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.active = False
        self.volume = 0.5  # Default volume
        self.slider_rect = pygame.Rect(300, 200, 200, 20)
        self.slider_button_rect = pygame.Rect(300 + int(self.volume * 200) - 5, 195, 10, 30)
        self.dragging = False
        self.font = pygame.font.Font(None, 36)

        self.load_settings()

    def load_settings(self):
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as f:
                data = json.load(f)
                self.volume = data.get("volume", 0.5)
                self.slider_button_rect.x = 300 + int(self.volume * 200) - 5
                pygame.mixer.music.set_volume(self.volume)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def draw(self):
        volume_label = self.font.render("Volume", True, (255, 255, 255))
        self.screen.blit(volume_label, (self.slider_rect.x, self.slider_rect.y - 30))
        pygame.draw.rect(self.screen, (255, 255, 255), self.slider_rect, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.slider_button_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.active:
            if self.slider_button_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.active:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.active:
            if self.dragging:
                self.slider_button_rect.x = min(max(event.pos[0], self.slider_rect.x), self.slider_rect.x + self.slider_rect.width)
                self.volume = (self.slider_button_rect.x - self.slider_rect.x) / self.slider_rect.width
                pygame.mixer.music.set_volume(self.volume)

    def save_settings(self):
        with open("settings.json", "w") as f:
            json.dump({"volume": self.volume}, f)
