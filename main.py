def is_pos_neg(n):
    if n > 0:
        print(f'Число {n} положительное!')
    elif n < 0:
        print(f'Число {n} отрицательное!')
    else:
        print('Это ноль!')
n = int(input())
is_pos_neg(n)