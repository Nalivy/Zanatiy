def power(x, y=2):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

try:
    x = int(input("x = "))
    y = int(input("y = "))
    if y < 0:
        print("Отрицательные степени пока не поддерживаются в этой версии.")
    else:
        print(power(x, y))
except ValueError:
    print("Ошибка: введите целые числа!")
except RecursionError:
    print("Ошибка: слишком глубокая рекурсия.")
except Exception as e:
    print("Другая ошибка:", e)
