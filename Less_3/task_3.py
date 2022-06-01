# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

lst = []
while len(lst) != 10:
    tmp = randint(1, 100)
    if tmp not in lst:
        lst.append(tmp)
lst_copy = lst.copy()
lst[lst_copy.index(min(lst_copy))] = max(lst_copy)
lst[lst_copy.index(max(lst_copy))] = min(lst_copy)
print(f'Список:\n'
      f'{lst_copy}\n'
      f'Минимальное значение: {min(lst_copy)}\n'
      f'Индекс минимального значения: {lst_copy.index(min(lst_copy))}\n'
      f'Максимальное значение: {max(lst_copy)}\n'
      f'Индекс максимального значения: {lst_copy.index(max(lst_copy))}\n\n'
      f'{"-" * 20} [Обработка] {"-" * 20}\n\n'
      f'Список:\n'
      f'{lst}\n'
      f'Минимальное значение: {min(lst)}\n'
      f'Индекс минимального значения: {lst.index(min(lst))}\n'
      f'Максимальное значение: {max(lst)}\n'
      f'Индекс максимального значения: {lst.index(max(lst))}')
