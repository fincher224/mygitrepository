while True:
    cont = ''
    try:
        while cont == '':
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
            cont = input('Нажмите Enter чтобы продолжть: ')
    except ValueError:
        print('Только числа!')
        cont = input('Нажмите Enter чтобы продолжить: ')
        continue
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        cont = input('Нажмите Enter чтобы продолжить: ')
        continue