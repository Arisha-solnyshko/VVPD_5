import math


def cos_taylor(x, terms=10):
    '''
    Вычисление косинуса числа х с использованием ряда Тейлора.

    Эта функция вычисляет приближенное значение косинуса числа x, используя
    разложение в ряд Тейлора. Для точности вычислений используется заданное
    количество членов ряда (по умолчанию 10).

    Аргументы:
    x - число (в радианах), для которого нужно вычислить косинус.
    terms - количество членов ряда Тейлора, которые используются для вычислений (по умолчанию 10).

    Возвращаемое значение:
    float - приближенное значение косинуса числа x.

    Исключения:
    Отсутствуют.

    Пример:
    >>> cos_taylor(0)
    1.0
    >>> cos_taylor(math.pi/3)
    0.5000000000000001
    '''
    cos = 0
    for n in range(terms):
        term = ((-1) ** n * x ** (2 * n)) / math.factorial(2 * n)
        cos += term
    return cos

def arctan_taylor_series(x, terms=10):
    '''
    Вычисление арктангенса числа x с использованием ряда Тейлора.

    Эта функция вычисляет приближенное значение арктангенса числа x, используя
    разложение в ряд Тейлора. При этом x должно быть в пределах от -1 до 1
    (включительно). Для точности вычислений используется заданное количество
    членов ряда (по умолчанию 10).

    Аргументы:
    x - число (в интервале [-1, 1]), для которого нужно вычислить арктангенс.
    terms -- количество членов ряда Тейлора, которые используются для вычислений (по умолчанию 10).

    Возвращаемое значение:
    float - приближенное значение арктангенса числа x.

    Исключения:
    ValueError - если x не находится в пределах от -1 до 1.

    Пример:
    >>> arctan_taylor_series(0)
    0.0
    >>> arctan_taylor_series(0.5)
    0.4636476090008061
    '''
    if not -1 <= x <= 1:
        raise ValueError("x должно быть в диапазоне [-1, 1]")
    result = 0
    for n in range(terms):
        term = ((-1) ** n * x ** (2 * n + 1)) / (2 * n + 1)
        result += term
    return result

def radians_to_degrees(radians):
    '''
    Перевод числа из радиан в градусы.

    Эта функция переводит значение угла из радиан в градусы.

    Аргументы:
    radians - угол в радианах.

    Возвращаемое значение:
    float - угол в градусах.

    Исключения:
    Отсутствуют.

    Пример:
    >>> radians_to_degrees(math.pi)
    180.0
    >>> radians_to_degrees(math.pi/2)
    90.0
    '''
    return radians * (180 / math.pi)

def main():
    '''
    Главная функция для запуска программы.

    Эта функция представляет собой меню выбора, где пользователь может
    выбрать одну из трёх доступных функций: вычисление косинуса или арктангенса
    с использованием ряда Тейлора. Программа запрашивает значение для переменной x,
    переводит его в градусы и выводит результат.

    Аргументы:
    Отсутствуют.

    Возвращаемое значение:
    Отсутствует.

    Исключения:
    Возможны исключения ValueError, если ввод неверный или выходит за пределы допустимых значений.

    Пример:
    (Пример работы программы будет на экране, пользователь выбирает функцию и вводит значения).
    '''
    print("Меню:")
    print("1. Косинус (с использованием ряда Тейлора)")
    print("2. Арктангенс (с использованием ряда Тейлора)")

    choice = input("Выберите функцию (1, 2 или 3): ")

    try:
        if choice == "1":
            x = float(input("Введите значение x (в радианах): "))
            x_degrees = radians_to_degrees(x)
            print(f"Значение x в градусах: {x_degrees:.2f}°")
            result = cos_taylor(x)
            print(f"Результат вычисления cos({x}) с использованием ряда Тейлора: {result:.6f}")
        elif choice == "2":
            x = float(input("Введите значение x (в интервале [-1, 1]): "))
            if not -1 <= x <= 1:
                print("Ошибка: x должно быть в диапазоне [-1, 1]")
            else:
                x_degrees = radians_to_degrees(x)
                print(f"Значение x в градусах: {x_degrees:.2f}°")
                result = arctan_taylor_series(x)
                print(f"Результат вычисления arctan({x}) с использованием ряда Тейлора: {result:.6f}")
        else:
            print("Неверный выбор, выберите 1 или 2.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    main()
