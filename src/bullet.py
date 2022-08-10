import pygame


class Bullet(pygame.sprite.Sprite):
    # Создание пули в позиции корабля
    def __init__(self, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        # Координаты пули, ширина и высота (в пикселях)
        self.rect = pygame.Rect(0, 0, 2, 12)
        # Цвет пули
        self.color = 255, 255, 0  # Желтый цвет (RGB код)
        # Скорость пули
        self.speed = 4.5
        # Синхронизация с кораблем (его верхней частью)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Изменение позиции пули
        self.y = float(self.rect.y)

    # Перемещение пули вверх
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    # Отрисовка пули на экране
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
