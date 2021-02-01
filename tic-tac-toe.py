a = '_________'
end_state = False
history = set()
print(f"""---------
| {a[0]} {a[1]} {a[2]} |
| {a[3]} {a[4]} {a[5]} |
| {a[6]} {a[7]} {a[8]} |
---------""")
matrix = [['1, 3'], ['2, 3'], ['3, 3'],
          ['1, 2'], ['2, 2'], ['3, 2'],
          ['1, 1'], ['2, 1'], ['3, 1']]
possible_moves = ('X', 'O')


def x_wins():
    if a[0] == a[1] == a[2] == 'X' \
            or a[3] == a[4] == a[5] == 'X' \
            or a[6] == a[7] == a[8] == 'X' \
            or a[0] == a[3] == a[6] == 'X' \
            or a[1] == a[4] == a[7] == 'X' \
            or a[2] == a[5] == a[8] == 'X' \
            or a[0] == a[4] == a[8] == 'X' \
            or a[2] == a[4] == a[6] == 'X':
        history.add('x')


def o_wins():
    if a[0] == a[1] == a[2] == 'O' \
            or a[3] == a[4] == a[5] == 'O' \
            or a[6] == a[7] == a[8] == 'O' \
            or a[0] == a[3] == a[6] == 'O' \
            or a[1] == a[4] == a[7] == 'O' \
            or a[2] == a[5] == a[8] == 'O' \
            or a[0] == a[4] == a[8] == 'O' \
            or a[2] == a[4] == a[6] == 'O':
        history.add('o')


def draw():
    if '_' not in a and 'x' not in history and 'o' not in history:
        history.add('draw')


def impossible():
    if 'x' in history and 'o' in history \
            or abs(a.count('X') - a.count('O')) >= 2:
        history.add('Impossible')


def result():
    x_wins()
    o_wins()
    draw()
    impossible()
    global end_state
    if any(history):
        if 'Impossible' in history:
            print('Impossible')
        elif 'x' in history:
            print('X wins')
        elif 'o' in history:
            print('O wins')
        elif 'draw' in history:
            print('Draw')
        end_state = True
    else:
        pass


def play():
    global a
    while True:
        try:
            x, y = input('Enter the coordinates:').split()
            x = int(x)
            y = int(y)
            if not 1 <= x <= 3 or not 1 <= y <= 3:
                print("Coordinates should be from 1 to 3!")
            else:
                num_of_cell = matrix.index([str(f'{x}, {y}')])
                if a[num_of_cell] == 'X' or a[num_of_cell] == 'O':
                    print("This cell is occupied! Choose another one!")
                else:
                    if a.count('X') != a.count('O'):
                        move = 'O'
                    else:
                        move = 'X'
                    if num_of_cell == 0:
                        a = f'{move}{a[1:]}'
                        break
                    elif num_of_cell == 8:
                        a = f'{a[:-1]}{move}'
                        break
                    else:
                        a = f'{a[:num_of_cell]}{move}{a[num_of_cell + 1:]}'
                        break

        except ValueError:
            print("You should enter numbers!")

    print(f"""---------
| {a[0]} {a[1]} {a[2]} |
| {a[3]} {a[4]} {a[5]} |
| {a[6]} {a[7]} {a[8]} |
---------""")
    result()


while not end_state:
    play()
