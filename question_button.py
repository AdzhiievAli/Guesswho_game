import pygame

class QuestionButton:
    def __init__(self, screen, position, size, questions):
        self.screen = screen
        self.rect = pygame.Rect(position, size)
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render('Показати питання', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.questions = questions
        self.showing_questions = False
        self.questions_display_rects = []
        self.background_rect = None

    def draw(self):
        pygame.draw.rect(self.screen, (0, 128, 0), self.rect)
        self.screen.blit(self.text, self.text_rect)
        if self.showing_questions:
            self.display_questions()

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.showing_questions = not self.showing_questions
            if self.showing_questions:
                self.text = self.font.render('Закрити питання', True, (255, 255, 255))
            else:
                self.text = self.font.render('Показати питання', True, (255, 255, 255))
            return True
        return False

    def display_questions(self):
        y_offset = 80
        questions_height = len(self.questions) * 40 + 20
        self.background_rect = pygame.Rect(self.rect.x - 10, y_offset - 10, self.rect.width + 400, questions_height)
        pygame.draw.rect(self.screen, (255, 255, 255), self.background_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.background_rect, 2)

        self.questions_display_rects = []
        for question in self.questions:
            question_text = self.font.render(question, True, (0, 0, 0))
            rect = question_text.get_rect(topleft=(self.rect.x, y_offset))
            self.questions_display_rects.append(rect)
            self.screen.blit(question_text, rect)
            y_offset += 40
