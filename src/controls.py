import pygame
import sys
import time
from bullet import Bullet
from alien import Alien  # модуль с классом пришельца


# Обработка действий пользователя
def events(screen, ship, bullets):
    for event in pygame.event.get():
        # Для закрытия окна с игрой
        if event.type == pygame.QUIT:
            sys.exit()

        # Действие - нажатие клавиши
        elif event.type == pygame.KEYDOWN:
            # Клавиша d (ВПРАВО)
            if event.key == pygame.K_d:
                # Меняем логическую переменную (смещаем корабль вправо по координате)
                ship.mright = True
            # Клавиша a (ВЛЕВО)
            elif event.key == pygame.K_a:
                # Меняем логическую переменную (смещаем корабль влево по координате)
                ship.mleft = True
            # Клавиша ПРОБЕЛ
            elif event.key == pygame.K_SPACE:
                # Создаем объект пули
                new_bullet = Bullet(screen, ship)
                # В pygame-контейнер добавляем объект
                bullets.add(new_bullet)

        # Действие - отжатие клавиши
        elif event.type == pygame.KEYUP:
            # Клавиша d (ВПРАВО)
            if event.key == pygame.K_d:
                # Меняем логическую переменную (перестаем смещать корабль вправо по координате)
                ship.mright = False
            # Клавиша a (ВЛЕВО)
            elif event.key == pygame.K_a:
                # Меняем логическую переменную (перестаем смещать корабль влево по координате)
                ship.mleft = False


# Обновление экрана
def update(bg_color, screen, stats, score, ship, aliens, bullets):
    # Фоновый цвет
    screen.fill(bg_color)
    # Вывод счета на экран
    score.show_score()
    # Вывод пуль на экран
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Вывод корабля на экран
    ship.output()
    # Вывод пришельца на экран
    aliens.draw(screen)
    # Прорисовка последнего экрана
    pygame.display.flip()


# Обновление позиции пуль
def update_bullets(screen, stats, score, aliens, bullets):
    bullets.update()
    # Удаление всех пуль, вышедших за пределы экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Проверка коллизии (столкновение пули и пришельца)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # True, True - удаление и пули, и пришельца
    # Увеличиваем счет на 1 за каждого сбитого пришельца
    if collisions:
        for aliens in collisions.values():
            stats.score += 1 * len(aliens)
        score.image_score()
        # Проверка на рекорд
        check_high_score(stats, score)
        # Вывод количества жизней
        score.image_ships()
    # Если все пришельцы уничтожены
    if len(aliens) == 0:
        # Очищаем пули
        bullets.empty()
        # Создаем новую армию пришельцев
        create_army(screen, aliens)


# Обновление позиции пришельцев
def update_aliens(stats, screen, score, ship, aliens, bullets):
    aliens.update()
    # Проверка на коллизию пришельца и корабля
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_kill(stats, screen, score, ship, aliens, bullets)
    # Проверка пересечения пришельца линии экрана
    aliens_check(stats, screen, score, ship, aliens, bullets)


# Создание армии пришельцев
def create_army(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    # Расчёт количества пришельцев в ряду, исходя из ширины экрана и модельки пришельца
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    # Расчет столбцов пришельцев
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)
    # Создаем строки
    for row_number in range(number_alien_y - 8):
        # Создаем ряды
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            # Добавляем в контейнер
            aliens.add(alien)


# Столкновение корабля и пришельцев
def ship_kill(stats, screen, score, ship, aliens, bullets):
    # Если жизней больше 0
    if stats.ships_left > 0:
        # Отнимаем одну жизнь и выводим новое число на экран
        stats.ships_left -= 1
        score.image_ships()
        # Очищаем экран
        aliens.empty()
        bullets.empty()
        # Заново создаем армию пришельцев и корабль
        create_army(screen, aliens)
        ship.create_ship()
        # Задержка при перезагрузке
        time.sleep(1)
    # В противном случае выходим из игры
    else:
        stats.run_game = False
        sys.exit()


# Проверка - дошли ли пришельцы до края экрана
def aliens_check(stats, screen, score, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        # Если у какого-то пришельца в прямоугольнике находится край экрана
        if alien.rect.bottom >= screen_rect.bottom:
            # Запускаем смерть корабля
            ship_kill(stats, screen, score, ship, aliens, bullets)
            break


# Проверка результата на рекорд
def check_high_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.image_high_score()
        # Запись рекорда в файл
        with open("highscore.txt", "w") as f:
            f.write(str(stats.high_score))
