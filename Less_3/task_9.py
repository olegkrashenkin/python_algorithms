# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

columns = randint(4, 9)
strings = randint(4, 9)
matrix = []
for i in range(columns):
    matrix.append([])
    for x in range(strings):
        matrix[i].append(randint(-100, 100))
print(f'Случайная матрица {strings} на {columns}:')
for string in matrix:
    for value in string:
        print(f'{value:^6}', end='')
    print()
tmp = []
for i in matrix[0]:
    tmp.append(i)
for string in matrix:
    idx = len(matrix[0]) - 1
    while idx >= 0:
        if string[idx] < tmp[idx]:
            tmp[idx] = string[idx]
        idx -= 1
print(f'{"-" * strings * 6}')
for i in tmp:
    print(f'{i:^6d}', end='')
print(f'\n{"-" * strings * 6}\n'
      f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max(tmp)}')
