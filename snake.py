import pygame
import random


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 1
        self.score = 0
        self.direction = "right"
        self.body = [(self.x, self.y)]

    def move(self):
        if self.direction == "right":
            self.x += 10
        elif self.direction == "left":
            self.x -= 10
        elif self.direction == "up":
            self.y -= 10
        elif self.direction == "down":
            self.y += 10

        self.body.append((self.x, self.y))

        if len(self.body) > self.length:
            del self.body[0]

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(x, y, 10, 10))

    def eat(self):
        self.length += 1
        self.score += 1

    def get_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.direction != "left":
            self.direction = "right"
        elif keys[pygame.K_LEFT] and self.direction != "right":
            self.direction = "left"
        elif keys[pygame.K_UP] and self.direction != "down":
            self.direction = "up"
        elif keys[pygame.K_DOWN] and self.direction != "up":
            self.direction = "down"

    def is_dead(self):
        head = self.body[-1]
        x, y = head

        if x < 5 or x >= 795 or y < 5 or y >= 595:
            return True

        if head in self.body[:-1]:
            return True

        return False
