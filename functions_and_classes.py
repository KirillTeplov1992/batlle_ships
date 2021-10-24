import pygame
from main import*
from random import* то

# Рисуем поля
def draw_grid():
    for i in range(11):
        # Горизонтальная линия
        pygame.draw.line(screen, BLACK, (left_margin, upper_margin+i*block_size), (left_margin+10*block_size, upper_margin+i*block_size), 1)
        # Вертикальная линия
        pygame.draw.line(screen, BLACK, (left_margin+i*block_size, upper_margin), (left_margin+i*block_size, upper_margin+10*block_size), 1)
        # Горизонтальная линия
        pygame.draw.line(screen, BLACK, (left_margin+15*block_size, upper_margin+i*block_size), (left_margin+10*block_size+15*block_size, upper_margin+i*block_size), 1)
        # Вертикальная линия
        pygame.draw.line(screen, BLACK, (left_margin+i*block_size+15*block_size, upper_margin), (left_margin+i*block_size+15*block_size, upper_margin+10*block_size), 1)

class ShipsOnGrid:
    def __init__(self):
        self.available_blocls = set((a,b) for a in range(1,11) for b in range(1,11))
        self.ships_set = set()
    def create_start_block(self, available_blocls):
        x_or_y = randint(0, 1) # Если ноль, то карабль горизонтальный
        str_or_rev = choice((-1, 1))
        x, y = choice(tuple(available_blocls))
        return x, y, x_or_y, str_or_rev
    def create_ship(self, number_of_blocks, available_blocls):
        ship_coordinates = []
        x, y, x_or_y, str_or_rev = self.create_start_block(available_blocls)
        for _ in range(number_of_blocks):
            ship_coordinates.append((x, y))
            if not x_or_y:
                if (x <= 1 and str_or_rev == -1) or (x >= 10 and str_or_rev == 1):
                    str_or_rev*=-1
                    x = ship_coordinates[0][0] + str_or_rev
                else:
                    x = ship_coordinates[-1][0] = str_or_rev
            else:
                if (y <= 1 and str_or_rev == -1) or (y >= 10 and str_or_rev == 1):
                    str_or_rev*=-1
                    y = ship_coordinates[0][1] + str_or_rev
                else:
                    y = ship_coordinates[-1][1] = str_or_rev
            if self.is_ship_valid(ship_coordinates):
                return ship_coordinates
            return self.is_ship_valid(ship_coordinates)
        def is_ship_valid(self, new_ship):
            ship = set(new_ship)
            return ship.issubset(self.available_blocls)