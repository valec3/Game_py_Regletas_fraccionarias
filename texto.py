import pygame

class Texto:
    def __init__(self, text, font_size, color, x, y):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.rendered_text, self.rect)