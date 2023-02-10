def intro():
    print('-----------------------')
    print('ДОБРО ПОЖАЛОВАТЬ В ИГРУ')
    print('    КРЕСТИКИ-НОЛИКИ    ')
    print('-----------------------')
    print('     Правила игры:     ')
    print('укажите координаты поля')
    print('x - по горизонтали')
    print('y - по вертикали')
    print('-----------------------')


m = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
count = 0


def field(m):
    print('  | 0 | 1 | 2 |')
    print(' ---------------')
    print(' 0|', m[0][0], '|', m[0][1], '|', m[0][2], '|\n',
          '---------------\n',
          '1|', m[1][0], '|', m[1][1], '|', m[1][2], '|\n',
          '---------------\n',
          '2|', m[2][0], '|', m[2][1], '|', m[2][2], '|\n',
          '---------------')


def steps():
    while True:
        moves = input('Ваш ход!').split()
        if len(moves) != 2:
            print('Введите две координаты')
            continue

        # x, y = moves
        if not moves[0].isdigit() or not moves[1].isdigit():
            print('Нужно ввести цифры')
            continue
        # x, y = int(x), int(y)
        x, y = map(int, moves)

        if 2 < x or x < 0 or 2 < y or y < 0:
            print('Координаты вне поля')
            continue

        if m[x][y] != ' ':
            print('Клетка уже занята')
            continue

        return x, y


def check_win():
    victory = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
               ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for i in victory:
        symbols = []
        for z in i:
            symbols.append(m[z[0]][z[1]])
        if symbols == ['X', 'X', 'X']:
            print('Победили крестики')
            return True
        if symbols == ['O', 'O', 'O']:
            print('Победили нолики')
            return True
    return False


while True:
    count += 1
    field(m)
    if count % 2 == 1:
        print('Ходят крестики')
    else:
        print('Ходят нолики')

    a, b = steps()
    if count % 2 == 1:
        m[a][b] = 'X'
    if count % 2 == 0:
        m[a][b] = 'O'
    if check_win():
        field(m)
        break
    if count == 9:
        print('Ничья')Раб
        break
