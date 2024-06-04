import pygame
import random
import os
from question_button import QuestionButton
from board import Board

class GuessWhoGame:
    def __init__(self, screen, pack):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        self.pack_path = os.path.join(os.getcwd(), pack)

        if not os.path.exists(self.pack_path):
            raise FileNotFoundError(f"Пак {pack} не знайдено")

        names_file_path = os.path.join(self.pack_path, 'names.txt')
        if not os.path.exists(names_file_path):
            raise FileNotFoundError(f"Пак {names_file_path} не знайдено")

        with open(names_file_path, 'r', encoding='utf-8') as file:
            card_names = [line.strip() for line in file.readlines()]

        questions_file_path = os.path.join(self.pack_path, 'questions.txt')
        if not os.path.exists(questions_file_path):
            raise FileNotFoundError(f"Пак {questions_file_path} не знайдено")

        with open(questions_file_path, 'r', encoding='utf-8') as file:
            questions = [line.strip() for line in file.readlines()]

        card_images = []
        for i in range(1, 13):
            image_path = os.path.join(self.pack_path, f'{i}.png')
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Зображення {image_path} не знайдено")
            card_images.append(pygame.image.load(image_path))

        self.board1 = Board(card_images, card_names, (50, 50))
        self.board2 = Board(card_images, card_names, (1050, 50))

        self.secret_card1 = random.choice(self.board1.cards)
        self.secret_card2 = random.choice(self.board2.cards)

        self.current_player = 1

        self.font = pygame.font.SysFont(None, 36)
        self.final_guess_button = pygame.Rect(800, 900, 200, 50)
        
        self.question_button1 = QuestionButton(screen, (50, 0), (200, 50), questions)
        self.question_button2 = QuestionButton(screen, (1550, 0), (200, 50), questions)

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1

    def draw_final_guess_button(self):
        pygame.draw.rect(self.screen, (0, 200, 0), self.final_guess_button)
        small_font = pygame.font.SysFont('Comic Sans MS', 20)
        text = small_font.render('Фінальна відповідь', True, (147, 112, 219))
        text_rect = text.get_rect(center=self.final_guess_button.center)
        self.screen.blit(text, text_rect)

    def draw_opponent_secret_card(self):
        text1 = self.font.render(f'Твоя секретна картка: {self.secret_card1.name}', True, (0, 0, 0))
        text2 = self.font.render(f'Твоя секретна картка: {self.secret_card2.name}', True, (0, 0, 0))
        self.screen.blit(text1, (50, 1050))
        self.screen.blit(text2, (1050, 1050))

    def final_guess(self, pos):
        if self.final_guess_button.collidepoint(pos):
            guess = None
            if self.current_player == 1:
                guess = self.secret_card2
            else:
                guess = self.secret_card1

            input_box = pygame.Rect(800, 600, 200, 50)
            color_inactive = pygame.Color('MediumPurple')
            color_active = pygame.Color('MediumPurple')
            color = color_inactive
            active = False
            text = ''
            done = False
            input_font = pygame.font.SysFont('Courier', 36)
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_box.collidepoint(event.pos):
                            active = not active
                        else:
                            active = False
                        color = color_active if active else color_inactive
                    if event.type == pygame.KEYDOWN:
                        if active:
                            if event.key == pygame.K_RETURN:
                                if text == guess.name:
                                    print(f'Player {self.current_player} wins!')
                                    winner_text = self.font.render(f'Player {self.current_player} wins!', True, (0, 255, 0))
                                else:
                                    print(f'Player {self.current_player} loses!')
                                    winner_text = self.font.render(f'Player {self.current_player} loses!', True, (255, 0, 0))
                                self.screen.fill((255, 255, 255))
                                self.screen.blit(winner_text, (960, 540))
                                pygame.display.flip()
                                pygame.time.wait(3000)
                                self.running = False
                                done = True
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode

                self.screen.fill((255, 255, 255))
                self.board1.draw(self.screen)
                self.board2.draw(self.screen)
                self.draw_final_guess_button()
                self.draw_opponent_secret_card()
                self.question_button1.draw()
                self.question_button2.draw()

                pygame.draw.rect(self.screen, color, input_box, 2)
                txt_surface = input_font.render(text, True, (0, 0, 0))
                width = max(200, txt_surface.get_width() + 10)
                input_box.w = width
                self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

                pygame.display.flip()
                self.clock.tick(30)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.final_guess_button.collidepoint(pos):
                        self.final_guess(pos)
                    elif self.question_button1.click(pos):
                        pass
                    elif self.question_button2.click(pos):
                        pass
                    else:
                        if self.current_player == 1:
                            card = self.board1.click(pos)
                        else:
                            card = self.board2.click(pos)

                        if card:
                            self.switch_player()

            self.screen.fill((255, 255, 255))
            self.board1.draw(self.screen)
            self.board2.draw(self.screen)
            self.draw_final_guess_button()
            self.draw_opponent_secret_card()
            self.question_button1.draw()
            self.question_button2.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
