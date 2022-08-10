# Отслеживание статистики
class Stats:
    def __init__(self):
        self.reset_stats()
        # Флаг под количество жизней больше нуля
        self.run_game = True
        # Самый высокий результат
        with open("highscore.txt", "r") as f:
            self.high_score = int(f.readline())

    # Статистика, изменяющаяся во время игры
    def reset_stats(self):
        self.ships_left = 2  # Количество жизней
        # Текущий счет
        self.score = 0
