def creation_field():  # Создание словаря с ключами-кортежами для координат
    g = [[(i, j) for j in range(0, 3)] for i in range(0, 3)]
    t = tuple(map(tuple, g))
    p = t[0] + t[1] + t[2]
    field = dict.fromkeys(p, "-")
    return field


game_field = creation_field()  # Создание игрового поля
player = ['X', 'O']  # Определение игроков


def visual_shell(): # Вывод на экран матрицы игрового поля
    global game_field
    r = game_field.values()
    game_field_visual = ((list(r))[0:3], (list(r))[3:6], (list(r))[6:9])
    for line in game_field_visual:
        print(*line)
    return None


print("Welcome!")  # Приветствие
visual_shell()  # Запуск визуализации


def any_all_ij(s):  # Условие равенства строк
    if any(all(game_field[(i, j)] == s for j in range(0, 3)) for i in range(0, 3)):
        return True


def any_all_ji(s):  # Условие равенства столбцов
    if any(all(game_field[(j, i)] == s for j in range(0, 3)) for i in range(0, 3)):
        return True


def reg_diag(s):  # Условие равенства элементов главной диагонали
    if all(game_field[(i, i)] == s for i in range(0, 3)):
        return True


def irreg_diag(s):  # Условие равенства элементов побочной диагонали
    if all(game_field[(1 + i, 1 - i)] == s for i in range(-1, 2)):
        return True


def restrictions(game_field_loc):  # Проверка, есть ли победитель
    if any(any_all_ij(S) or any_all_ji(S) or reg_diag(S) or irreg_diag(S) for S in player):
        return "someone won"
    elif "-" not in game_field_loc.values():
        return "Draw!"
    else:
        return None


def input_is_correct(reply_row, reply_column):  # Правильно ли введены координаты, и если нет - какую ошибку выдать
    if any(k not in ['1', '2', '3'] for k in [reply_row, reply_column]):
        return 0
    if 0 < int(reply_row) < 4 and 0 < int(reply_column) < 4:
        if game_field[(int(reply_row) - 1, int(reply_column) - 1)] == '-':
            return 2
        return 1
    else:
        return 0


def playing_the_game():  # Основной цикл игры
    global game_field
    while True:
        if restrictions(game_field) == "Draw!" or restrictions(game_field) == "someone won":
            break
        for i in player:
            if restrictions(game_field) == "Draw!":
                print("Draw!")
                break
            elif restrictions(game_field) == "someone won":
                print("'%s' won!" % set(player).difference(i))
                break
            reply_row, reply_column = input("'%s' player makes a move. Please select a row: " % i), input(
                "Please select a column: ")
            if input_is_correct(reply_row, reply_column) == 2:
                game_field[(int(reply_row) - 1, int(reply_column) - 1)] = '%s' % i
            elif input_is_correct(reply_row, reply_column) == 1:
                print("You can't change this cell")
            else:
                print("Wrong cell")
            visual_shell()
        continue


playing_the_game()  # Запуск игры
