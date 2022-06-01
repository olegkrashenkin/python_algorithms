# Определить, какое число в массиве встречается чаще всего.

from random import randint

lst = []
while len(lst) != 15:
    lst.append(randint(1, 70))
print(f'Список:\n'
      f'{lst}\n'
      f'{"-" * 50}')


def count_num(list_):
    """
    Поиск самых частоповторяющихся чисел в массиве,
    если таких чисел несколько, например a = [1, 1, 2, 3, 3],
    то функция выведет на экран и число 1 и число 3, т.к. они
    встречаются в массиве чаще всего.
    """
    lst = list_.copy()
    num = 0
    cnt = 0
    for i in lst:
        if lst.count(i) > cnt:
            num = i
            cnt = lst.count(i)
    if cnt == 1:
        print('В массиве нет повторяющихся чисел!')
    else:
        print(f'Чаще всего встречается число {num}: {cnt} раз(а)')
        for i in range(cnt):
            lst.remove(num)
        for i in lst:
            if lst.count(i) == cnt:
                count_num(lst)
                break


if __name__ == '__main__':
    count_num(lst)
