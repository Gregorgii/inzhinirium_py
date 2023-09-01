from snake import *
from apple import *
from database import *
from random import randrange


class Game:
    def __init__(self):
        pygame.init()
        self.nickname = self.get_nickname()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.is_running = True
        pygame.time.wait(3000)
        x = randrange(1, 400, 10)
        y = randrange(1, 500, 10)
        self.snake = Snake(x, y)
        x = randrange(1, 700, 10)
        y = randrange(1, 500, 10)
        self.apple = Apple(x, y)
        self.db = Database()
        self.db.create_table()
        pygame.font.Font(None, 36)

    def get_nickname(self):
        nickname = input("Enter your nickname: ")
        print("Go to window with game. "
              "It's Snake, you know this game. Press the arrows and collect apples.")
        return nickname

    def run(self):
        global font
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            if self.snake.is_dead() is True:
                self.db.insert_score(self.nickname, self.snake.score)
                text = font.render("Game Over", True, (255, 0, 0))
                text_rect = text.get_rect(center=(400, 300))
                self.screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(2000)
                self.screen.fill((0, 0, 0))
                pygame.display.flip()
                for i in range(len(self.db.get_top_scores())):
                    text = font.render(self.db.get_top_text(i), True, (255, 0, 0))
                    text_rect = text.get_rect(center=(400, 100 * (2 + i/2)))
                    self.screen.blit(text, text_rect)
                    pygame.display.update()
                pygame.time.wait(5000)
                self.is_running = False

            if self.snake.score == 1000:
                text = font.render("Winner-winner chicken dinner", True, (255, 0, 0))
                text_rect = text.get_rect(center=(400, 300))
                self.screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(2000)
                self.is_running = False

            self.screen.fill((0, 125, 255))

            if self.snake.body[-1] == self.apple.body:
                self.snake.eat()
                self.apple.update(randrange(1, 700, 10), randrange(1, 500, 10))

            self.snake.get_direction()
            self.snake.move()
            self.snake.draw(self.screen)
            self.apple.draw(self.screen)

            font = pygame.font.Font(None, 24)
            score_text = font.render("Score: " + str(self.snake.score), True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
