import pygame


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.color = (255, 0, 0)
        self.body = (self.x, self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def update(self, x, y):
        self.x = x
        self.y = y
        self.body = (x, y)


