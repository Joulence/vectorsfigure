#Funtions \ Функции

#English Version

def triangle1():
    a = float(input("Side 1: "))
    b = float(input("Side 2: "))
    c = float(input("Side 3: "))


    if a > b + c or b > a + c or c > a + b:
        print("Triangle doesn't exist")
        # Equilateral Triangle
    elif a == b == c:
        print("Equilateral Triangle")
    # Isosceles Triangle
    elif a == b != c or a == c != b or b == c != a:
        print("Isosceles Triangle")
    # Right Triangle
    elif a ** 2 == c ** 2 - b ** 2 or c ** 2 == a ** 2 + b ** 2 or b ** 2 == c ** 2 - a ** 2:
        print("Right Triangle")
        # Scalene Triangle
    elif a < b + c or b < a + c or c < a + b:
        print("Scalene Triangle")

    repeat = input("Reapet - y\nExit - n\n")
    if repeat == "y":
        triangle1()
    elif repeat == "n":
        print("Shutting down")

#Русская Версия

def triangle2():
    a = float(input("Сторона 1: "))
    b = float(input("Сторона 2: "))
    c = float(input("Сторона 3: "))

    if a > b + c or b > a + c or c > a + b:
        print("Треугольник не существует")
    # Правильный треугольник
    elif a == b == c:
        print("Правильный треугольник")
    # Равнобедренный
    elif a == b != c or a == c != b or b == c != a:
        print("Равнобедренный")
    # Прямоугольный треугольник
    elif a ** 2 == c ** 2 - b ** 2 or c ** 2 == a ** 2 + b ** 2 or b ** 2 == c ** 2 - a ** 2:
        print("Прямоугольный треугольник")
        # Простой треугольник
    elif a < b + c or b < a + c or c < a + b :
        print("Простой треугольник")

    print("=========================================")
    repeat = input("Повторить - д\nЗакончить - н\n")
    if repeat == "д":
        triangle2()
    elif repeat == "н":
        print("Выключение")

#Program begin \ Начало программы

print("=========================================")
print("Figure calculation \ Вычисление фигуры")
print("=========================================")
print("Hello, choose the language!\nПривет, выбери язык")
start = input("1 - English\n2 - Русский\n=========================================\n")

if start == "1":
    triangle1()

if start == "2":
    triangle2()


print("=========================================")