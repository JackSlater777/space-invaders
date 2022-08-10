import pygame
import controls  # модуль обработки действий пользователя
from ship import Ship  # модуль с классом корабля
from pygame.sprite import Group
from stats import Stats  # модуль с классом статистики
from scores import Scores  # модуль с классом счета


# Запуск окна с игрой
def run():
    pygame.init()
    # Устанавливаем размер окна с игрой
    screen = pygame.display.set_mode((700, 800))
    # Устанавливаем заголовок для графического окна
    pygame.display.set_caption("Space Invaders")
    # Устанавливаем фоновый цвет для окна
    bg_color = (0, 0, 0)  # RGB-формат, 0 0 0 - черный
    # Создаем объект класса корабль
    ship = Ship(screen)
    # Создаем объект класса пуля
    bullets = Group()
    # Создаем объект класса пришелец
    aliens = Group()
    # Создаем армию пришельцев
    controls.create_army(screen, aliens)
    # Создаем объект класса статистики
    stats = Stats()
    # Создаем объект класса счета
    score = Scores(screen, stats)

    # Главный цикл игры
    while True:
        # Запуск модуля с обработкой действий игрока
        controls.events(screen, ship, bullets)
        # Проверка флага (количество жизней больше 0)
        if stats.run_game:
            # Обновление позиции корабля
            ship.update_ship()
            # Обновление экрана
            controls.update(bg_color, screen, stats, score, ship, aliens, bullets)
            # Обновление пуль
            controls.update_bullets(screen, stats, score, aliens, bullets)
            # Обновление пришельцев
            controls.update_aliens(stats, screen, score, ship, aliens, bullets)


run()
