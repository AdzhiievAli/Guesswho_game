import pygame

class Button:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.font = pygame.font.Font(None, 36)
        self.width, self.height = 200, 50

    def draw(self, screen):
        rect_position = (
            self.position[0], 
            self.position[1], 
            self.width, 
            self.height
        )
        pygame.draw.rect(screen, (255, 255, 255), rect_position, 2)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_x = self.position[0] + self.width // 2 - text_surface.get_width() // 2
        text_y = self.position[1] + self.height // 2 - text_surface.get_height() // 2
        text_position = (text_x, text_y)
        screen.blit(text_surface, text_position)

    def is_clicked(self, mouse_pos):
        button_right = self.position[0] + self.width
        button_bottom = self.position[1] + self.height
        is_click = (
            self.position[0] < mouse_pos[0] < button_right and
            self.position[1] < mouse_pos[1] < button_bottom
        )
        return is_click