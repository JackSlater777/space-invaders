import pygame.font
from ship import Ship
from pygame.sprite import Group


# Вывод игрового счета
class Scores:
    # Инициализация подсчета очков
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        # Текст счета: цвет и тип шрифта
        self.text_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 36)  # None - тип по умолчанию, 36 - размер
        # Отрисовка на экране
        self.image_score()
        # Отрисовка рекорда на экране
        self.image_high_score()
        # Отрисовка жизней на экране
        self.image_ships()

    # Преобразование текста счета в изображение
    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    # Преобразование рекорда в изображение
    def image_high_score(self):
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    # Вывод количества жизней на экран
    def image_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen)
            # Координаты
            ship.rect.x = 15 + ship_number * ship.rect.width
            ship.rect.y = 20
            # Добавляем в коллекцию каждый корабль
            self.ships.add(ship)

    # Вывод счета на экран
    def show_score(self):
        # Счет
        self.screen.blit(self.score_img, self.score_rect)
        # Рекорд
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # Жизни
        self.ships.draw(self.screen)
