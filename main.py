import random
import sys

import pygame


def draw():
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width, random.random() * height, 1, 1))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    running = True
    x = width // 2
    y = height // 2
    x_2 = width // 2
    y_2 = height // 2
    v = 30  # пикс в сек
    fps = 60
    clock = pygame.time.Clock()
    # font = pygame.font.SysFont(None, 40)
    screen.fill(pygame.Color('blue'))
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():

            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill(pygame.Color('blue'))

                    x+=random.randrange(random.randrange(-30, -1), random.randrange(0, 30))
                    y+=random.randrange(random.randrange(-30, -1), random.randrange(0, 30))
                    x_2+=random.randrange(random.randrange(-30, -1), random.randrange(0, 30))
                    y_2+=random.randrange(random.randrange(-30, -1), random.randrange(0, 30))
                    pygame.draw.circle(screen, pygame.Color('orange'), (x % width, y % height), 30)
                    pygame.draw.circle(screen, pygame.Color('white'), (x_2 % width, y_2 % height), 30)
                    
            # clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


