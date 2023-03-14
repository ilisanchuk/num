def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print(f"Год {y} является високосным.")
    else:
        print(f"Год {y} не високосный.")
y = int(input('Введите число: '))
is_leap_year(y)