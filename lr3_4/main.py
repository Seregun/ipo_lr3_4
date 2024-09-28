import math # Добавление модуля math
a = float(input("Введите число a: ")) # Ввод числа a
b = float(input("Введите число b: ")) # Ввод числа b
c = float(input("Введите число c: ")) # Ввод числа c
D = b**2 - 4*a*c # Подсчет дискриминанта
if D > 0: # Дискриминант больше нуля
    x1 = (-b + math.sqrt(D)) / (2 * a) # Подсчет первого корня
    x2 = (-b - math.sqrt(D)) / (2 * a) # Подсчет второго корня
    print(f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}") # Вывод корней
elif D == 0: # Дискриминант равен нулю
    x = -b / (2 * a) # Подсчет корня
    print(f"Уравнение имеет один корень: x = {x}") # Вывод корня
else: # Дискриминант меньше нуля
    print("Уравнение не имеет корней.") # Вывод сообщения об отсутствии корней