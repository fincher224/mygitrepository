while True:
    cont = 'y'
    try:
        while cont == 'y':
            a = float(input('Введите число: '))
            b = input('Введите операцию: ')
            c = float(input('Введите второе число: '))
            if b == '+':
                print(f'Результат: {a + c}')
            elif b == '-':
                print(f'Результат: {a - c}')
            elif b == '*':
                print(f'Результат: {a * c}')
            elif b == '/':
                print(f'Результат: {a / c}')
            elif b == '**':
                print(f'Результат: {a ** c}')
            elif b == '//':
                print(f'Результат: {a // c}')
            elif b == '%':
                print(f'Результат: {a % c}')
            elif b == '==':
                print(f'Результат: {a == c}')
            else:
                print('Некорректная операция')
            cont = input('Нажмите любую клавишу чтобы продолжть: ')
    except ValueError:
        print('Только числа!')
        cont = input('Нажмите любую клавишу чтобы продолжить: ')
        continue
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        cont = input('Нажмите любую клавишу чтобы продолжить: ')
        continue