# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from pprint import pprint


sudoku = (
    [0, 0, 0, 0, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 3, 0, 0, 0, 0, 0],
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
                return False


def possible_numbers(table, row, col):
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

    # не будем учитывать цифру, стоящую на этой позиции
    table_row = list(table[row])
    table_row.remove(table[row][col])

    forbidden_numbers_set = set(table_row).union(set(col_nums)).union(square_nums)
    return sorted(list(numbers_set.difference(forbidden_numbers_set)))


def solve(sudoku_table):
    empties = get_all_empty(sudoku_table)
    if not empties:
        pprint(sudoku_table)
        exit()
    ne = empties[0]
    pn = possible_numbers(sudoku_table, ne[0], ne[1])
    while pn:
        for num in pn:
            sudoku_table[ne[0]][ne[1]] = num
            solve(sudoku_table)
        sudoku_table[ne[0]][ne[1]] = 0
        break
    return sudoku_table


solve(sudoku)
