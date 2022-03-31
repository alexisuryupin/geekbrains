number = input('Введите число: ')

sum = 0
multiplication = 1
for i in number:
    sum += int(i)
    multiplication *= int(i)

print(f"Сумма цифр числа {number}: {sum}")
print(f'Произведение чисел {number}: {multiplication}')
