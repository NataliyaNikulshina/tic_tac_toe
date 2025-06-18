# Объявить класс.
class Board:
    """Класс, который описывает игровое поле."""
    # Новый атрибут.
    field_size = 3
    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы - это пустые клетки.

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        # Цикл проходится по всем столбцам игрового поля.
        for i in range(self.field_size):
            # А потом по всем строчкам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True

    # Этот метод будет определять победу.
    def check_win(self, player):
        # Проверка по горизонталям и вертикалям
        for i in range(self.field_size):
            if (all([self.board[i][j] == player for j in
                     range(self.field_size)]) or
                    all([self.board[j][i] == player for j in
                         range(self.field_size)])):
                return True
        # Проверка по диагоналям
        if (all([self.board[i][i] == player for i in
                range(self.field_size)]) or
                all([self.board[i][self.field_size - 1 - i] == player
                     for i in range(self.field_size)])):
            return True
        return False

    # Переопределяем метод __str__.
    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
