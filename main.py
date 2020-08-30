# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


sudoku = (
    [0, 0, 0, 1, 0, 5, 0, 6, 8],
    [0, 0, 0, 0, 0, 0, 7, 0, 1],
    [9, 0, 1, 0, 0, 0, 0, 3, 0],
    [0, 0, 7, 0, 2, 6, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 8, 7, 0, 4, 0, 0],
    [0, 3, 0, 0, 0, 0, 8, 0, 5],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [7, 9, 0, 4, 0, 1, 0, 0, 0],
)


def get_all_empty(table):
    empty_list = list()
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                empty_list.append([i, j])
    return empty_list


def next_empty(row=0, col=0):
    row = row if col < 8 else row + 1
    for r in range(row, 9):
        col = col + 1 if col < 8 else 0
        for c in range(col, 9):
            if sudoku[r][c] == 0:
                return r, c
            else:
                'done'


def possible_numbers(table, row=0, col=0):
    numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    col_nums = list()

    # собираем уже существующие цифры по столбцам и строкам
    for r in table:
        if table.index(r) != row:
            col_nums.append(r[col])

    # собираем уже существующие цифры в квадранте
    start_row = row // 3 * 3
    start_col = col // 3 * 3
    square_nums = list()
    for i in range(3):
        for j in range(3):
            square_nums.append(table[start_row + i][start_col + j])

    forbidden_numbers_set = set(table[row]).union(set(col_nums)).union(square_nums)
    return sorted(list(numbers_set.difference(forbidden_numbers_set)))


def try_number(position, possible_numbers):



def solve(table, depth=0):
    empty_positions = get_all_empty(table)
    solved_table = table

    while depth != len(empty_positions):
        for e in empty_positions:

            

    possib_solut = possible_numbers(solved_table, empty_positions[depth][0], empty_positions[depth][1])
    if possib_solut:
        for num in possib_solut:
            solved_table[empty_positions[0][0]][empty_positions[0][1]] = num
            attempt(solved_table, depth + 1)
    return solved_table


print(attempt(sudoku))
