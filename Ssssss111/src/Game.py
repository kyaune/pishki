import pygame 

from src.Config import*
from src.Snake import Snake
from src.Apple import Apple

class Game:
    def __init__(self, display):
        self.display = display
        self.score = 0

    def loop(self):
        clock = pygame.time.Clock()
        snake = Snake(self.display)
        apple = Apple(self.display)

        x_change = 0
        y_change = 0
        
        self.score = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -SNAKE_SPEED
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = SNAKE_SPEED
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        x_change = 0
                        y_change = -SNAKE_SPEED
                    elif event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = SNAKE_SPEED
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    apple.randomize()
                    self.score += 1
        
            self.display.fill(BLUE)
            
            pygame.draw.rect(
                self.display, 
                BLACK,
                [
                    BUMPER_SIZE,
                    BUMPER_SIZE,
                    HEIGHT - BUMPER_SIZE * 2,
                    WIDTH - BUMPER_SIZE * 2
                ]
            )
            
            apple_rect = apple.draw()

            snake.move(x_change, y_change)
            snake_rect = snake.draw()
            # snake.draw_body()

            bumper_x = WIDTH - BUMPER_SIZE
            bumper_y = HEIGHT - BUMPER_SIZE

            if (
                snake.x_pos < BUMPER_SIZE or
                snake.y_pos < BUMPER_SIZE or
                snake.x_pos + SNAKE_WIDTH > bumper_x or
                snake.y_pos + SNAKE_HEIGHT > bumper_y
            ):
                self.loop()

            if apple_rect.colliderect(snake_rect):
                apple.randomize()
                self.score += 1
                # snake.eat()

            # if len(snake.body) >= 1:
            #     for cell in snake.body:
            #         if snake.x_pos == cell[0] and snake.y_pos == cell[1]:
            #             self.loop()

            pygame.font.init()
            font = pygame.font.Font('./assets/Now-Regular.otf', 28)
            
            score_text = 'Score: {}'.format(self.score)
            score = font.render(score_text, True, WHITE)
            title = font.render('Sssssss', True, WHITE)


            title_rect = title.get_rect(
                center=(
                    WIDTH / 2, 
                    BUMPER_SIZE / 2
                )
            )

            score_rect = score.get_rect(
                center=(
                    500/2, 
                    HEIGHT - BUMPER_SIZE / 2
                )
            )

            self.display.blit(score, score_rect)
            self.display.blit(title, title_rect)

            pygame.display.update()
            clock.tick(FPS)