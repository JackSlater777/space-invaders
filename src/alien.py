import pygame


# Класс одного пришельца
class Alien(pygame.sprite.Sprite):
    def __init__(self, screen):
        # Задаем начальную позицию
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/alien.png")
        # Задаем "прямоугольник" пришельца
        self.rect = self.image.get_rect()
        # Прописываем координаты
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # Вывод пришельцев на экран
    def draw(self):
        self.screen.blit(self.image, self.rect)

    # Обновление координат пришельцев (движутся на корабль)
    def update(self):
        self.y += 0.05
        self.rect.y = self.y
