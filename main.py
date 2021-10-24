import pygame
from functions_and_classes import*

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

block_size = 30
left_margin = 40
upper_margin = 50

size = (left_margin + 30*block_size, upper_margin + 15*block_size)

def draw_grid():
    for y in range(11):
        for x in range(11):
            # Горизонтальная линия
            pygame.draw.line(screen, BLACK, (left_margin, upper_margin+y*block_size), (left_margin+10*block_size, upper_margin+y*block_size), 1)
            # Вертикальная линия
            pygame.draw.line(screen, BLACK, (left_margin+x*block_size, upper_margin), (left_margin+x*block_size, upper_margin+10*block_size), 1)
            # Горизонтальная линия
            pygame.draw.line(screen, BLACK, (left_margin+15*block_size, upper_margin+y*block_size), (left_margin+10*block_size+15*block_size, upper_margin+y*block_size), 1)
            # Вертикальная линия
            pygame.draw.line(screen, BLACK, (left_margin+x*block_size+15*block_size, upper_margin), (left_margin+x*block_size+15*block_size, upper_margin+10*block_size), 1)

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Морской бой")

def main():
    game_over = False
    screen.fill(WHITE)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        draw_grid()
        pygame.display.update()

main()
pygame.quit()