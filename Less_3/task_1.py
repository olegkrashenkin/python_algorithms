# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

nums = [i for i in range(2, 100)]
result_dict = {}
for i in nums:
    cnt = 2
    while cnt != 10:
        result_dict.setdefault(cnt, 0)
        if i % cnt == 0:
            result_dict[cnt] += 1
        cnt += 1
for k, v in result_dict.items():
    print(f'Кратны {k}: {v}')