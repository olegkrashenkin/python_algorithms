# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введите трехзначное число: ')
sum_result = 0
prod_result = 1
for num in number:
    num = int(num)
    sum_result += num
    prod_result *= num
print(f'[+]Сумма цифр числа {number} = {sum_result}\n'
      f'[*]Произведение цифр числа {number} = {prod_result}')
