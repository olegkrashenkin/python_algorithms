# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []
for i in range(5):
    matrix.append(list(map(int, input(f'Введите через пробел элементы {i+1} строки: ').split())))
    matrix[i].append(sum(matrix[i]))
print('-' * 40)
for string in matrix:
    for value in string:
        print(f'{value:^6}', end='')
    print()
