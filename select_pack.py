import pygame

def select_pack(screen):
    font = pygame.font.SysFont(None, 48)
    packs = ['Фрукти', 'Овочі']
    selected_pack = None
    running = True

    while running:
        screen.fill((255, 255, 255))
        y = 200
        for pack in packs:
            text = font.render(pack, True, (0, 0, 0))
            rect = text.get_rect(center=(screen.get_width() // 2, y))
            screen.blit(text, rect)
            y += 100

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                y = 200
                for pack in packs:
                    rect = pygame.Rect((screen.get_width() // 2 - 100, y - 25, 200, 50))
                    if rect.collidepoint(event.pos):
                        selected_pack = 'fruits_pack' if pack == 'Фрукти' else 'veg_pack'
                        running = False
                    y += 100

    return selected_pack
