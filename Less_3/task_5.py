# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

lst = []
while len(lst) != 10:
    tmp = randint(-100, 100)
    if tmp not in lst:
        lst.append(tmp)
result = max(filter(lambda x: x < 0, lst))
print(f'Список:\n'
      f'{lst}\n'
      f'Максимальный отрицательный элемент: {result}\n'
      f'Индекс максимального отрицательного элемента: {lst.index(result)}')
