import pygame
import os
import sys
from button import Button
from settings import Settings
from menu import Menu
from main_logic import GuessWhoGame
from select_pack import select_pack

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.current_menu = "main"
        self.music_path = os.path.join("bg_music1.mp3")

        self.main_menu_buttons = [
            Button("Play", (1000, 200)),
            Button("Options", (1000, 280)),
            Button("Credits", (1000, 360)),
            Button("Exit", (1000, 440))
        ]

        self.settings_menu_buttons = [
            Button("Back", (1000, 500))
        ]

        self.credits_menu_buttons = [
            Button("Back", (1000, 500))
        ]

        self.settings = Settings(screen)
        self.main_menu = Menu(screen, self.main_menu_buttons)
        self.settings_menu = Menu(screen, self.settings_menu_buttons, title="Settings")
        self.credits_menu = Menu(screen, self.credits_menu_buttons, title="Credits: made by Ali and Vlad")

    def play_music(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def run(self):
        pygame.mixer.init()
        self.play_music()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop_music()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.current_menu == "main":
                        for button in self.main_menu_buttons:
                            if button.is_clicked(pygame.mouse.get_pos()):
                                self.handle_main_menu_click(button)
                    elif self.current_menu == "settings":
                        for button in self.settings_menu_buttons:
                            if button.is_clicked(pygame.mouse.get_pos()):
                                self.handle_settings_menu_click(button)
                        self.settings.handle_event(event)
                    elif self.current_menu == "credits":
                        for button in self.credits_menu_buttons:
                            if button.is_clicked(pygame.mouse.get_pos()):
                                self.handle_credits_menu_click(button)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.current_menu == "settings":
                        self.settings.handle_event(event)

                elif event.type == pygame.MOUSEMOTION:
                    if self.current_menu == "settings":
                        self.settings.handle_event(event)

            self.draw_menu()
            pygame.display.flip()

    def draw_menu(self):
        if self.current_menu == "main":
            self.main_menu.draw()
        elif self.current_menu == "settings":
            self.settings_menu.draw()
            self.settings.draw()
        elif self.current_menu == "credits":
            self.credits_menu.draw()

    def handle_main_menu_click(self, button):
        if button.text == "Play":
            pack = select_pack(self.screen)
            game = GuessWhoGame(self.screen, pack)
            result = game.run()
            if result == "menu":
                self.current_menu = "main"
        elif button.text == "Options":
            self.current_menu = "settings"
            self.settings.activate()
        elif button.text == "Credits":
            self.current_menu = "credits"
        elif button.text == "Exit":
            self.stop_music()
            pygame.quit()
            sys.exit()

    def handle_settings_menu_click(self, button):
        if button.text == "Back":
            self.current_menu = "main"
            self.settings.deactivate()
            self.settings.save_settings()

    def handle_credits_menu_click(self, button):
        if button.text == "Back":
            self.current_menu = "main"
