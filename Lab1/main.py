import math
 
# Функция, которая принимает 3 коэффициента и возвращает два корня
def solve_quadratic_equation(a, b, c):
    # Вычисление дискриминанта
    d = (b**2) - (4*a*c)
 
    # Если дискриминант меньше нуля, то корней нет
    if d < 0:
        print("This equation has no real solution")
        return None, None
 
    # Вычисление корней
    root_1 = (-b + math.sqrt(d)) / (2*a)
    root_2 = (-b - math.sqrt(d)) / (2*a)
 
    return root_1, root_2
 
# Тестирование функции
# Пример 1
a = 1
b = 5
c = 6
root_1, root_2 = solve_quadratic_equation(a, b, c)
print(f"Root 1 = {root_1}")
print(f"Root 2 = {root_2}")