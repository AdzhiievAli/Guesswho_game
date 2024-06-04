from card import Card

class Board:
    def __init__(self, card_images, card_names, start_pos):
        self.cards = []
        x, y = start_pos
        for i in range(4):
            for j in range(3):
                pos = (x + j * 250, y + i * 250) 
                card = Card(card_images[i * 3 + j], card_names[i * 3 + j], pos)
                self.cards.append(card)

    def draw(self, screen):
        for card in self.cards:
            card.draw(screen)

    def click(self, pos):
        for card in self.cards:
            if card.click(pos):
                return card
        return None
