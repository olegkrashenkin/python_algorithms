# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

lst = []
while len(lst) != 10:
    tmp = randint(1, 100)
    if tmp not in lst:
        lst.append(tmp)
print(f'Список:\n'
      f'{lst}\n'
      f'Сумма элементов(кроме min и max): {sum(lst) - (max(lst) + min(lst))}')