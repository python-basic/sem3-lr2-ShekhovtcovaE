"""
    Написать программу по вычисленю площади треугольника по формуле Герона
"""


def main():
    flag_enter = True
    while flag_enter:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))
        if a + c > b and a + b > c and c + b > a:
            flag_enter = False
            result = geron(a, b, c)
            print("Площадь треугольника: ", result)
        else:
            print("Треугольник не существует. Попробуйте ввести другие данные")


def geron(a, b, c):
    """
    Расчет площади треугольника по формуле Герона
    a, b, c -стороны треугольника
    """
    p = a + b + c
    result = pow(p * (p-a) * (p-b) * (p-c), 0.5)
    return result
main()
