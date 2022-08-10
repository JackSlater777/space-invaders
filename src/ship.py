import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    # Инициализация корабля
    def __init__(self, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/ship.png")
        # Задаем "прямоугольник" корабля
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Прописываем координаты
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        # Задаем логические переменные для проверки нажатия клавиши (нужно для непрерывного движения)
        self.mright = False
        self.mleft = False

    # Вывод (отрисовка) корабля
    def output(self):
        self.screen.blit(self.image, self.rect)

    # Обновление позиции корабля
    def update_ship(self):
        # Если клавиша ВПРАВО нажата и координата корабля меньше, чем конец экрана
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1
        # Если клавиша ВЛЕВО нажата и координата корабля больше, чем конец экрана
        if self.mleft and self.rect.left > 0:
            self.center -= 1

        self.rect.centerx = self.center

    # Спавн нового корабля после смерти
    def create_ship(self):
        self.center = self.screen_rect.centerx
