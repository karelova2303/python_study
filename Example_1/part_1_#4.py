# Задача 4
# Дан треугольник ABC на плоскости, заданный координатами своих вершин. Для этого треугольника вычислить:
# радиус вписанной в треугольник окружности;
# радиус описанной вокруг треугольника окружности;
# сумму длин трех медиан треугольника.

# Реализация задачи
# 1. Импортировать функцию для перевода радиан в градусы, арккосинуса и квадратного корня.
from math import sqrt, pow

#2. Реализовать функцию для вычисления длины отрезка с координатами концов(x0, y0) и(x1, y1).
def compute_len(x_0, y_0, x_1, y_1):
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line

#3. Реализовать функцию для вычисления площади треугольника
def compute_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return area

#4. Реализовать функцию для вычисления радиуса вписанной в треугольник окружности:
def compute_radius_in_around(a, b, c):
    p = (a + b + c) / 2
    r = sqrt((p - a) * (p - b) * (p - c) / p)
    return r

#5. Реализовать функцию для вычисления радиуса описанной вокруг треугольника окружности:
def compute_radius_desc_around(a, b, c):
    R = (a * b * c) / (4 * compute_area(a, b, c))
    return R

#6. Длины медиан треугольника:
def compute_len_median(a, b, c):
    len_median_a = 0.5 * sqrt(2 * (pow(c, 2) + pow(b, 2)) - pow(a, 2))
    len_median_b = 0.5 * sqrt(2 * (pow(a, 2) + pow(c, 2)) - pow(b, 2))
    len_median_c = 0.5 * sqrt(2 * (pow(a, 2) + pow(b, 2)) - pow(c, 2))
    sum_len_median = len_median_a + len_median_b + len_median_c
    return sum_len_median

#7. Ввести координаты вершин треугольника с подсказкой пользователю.
x_a = float(input("x_a = "))
y_a = float(input("y_a = "))
x_b = float(input("x_b = "))
y_b = float(input("y_b = "))
x_c = float(input("x_c = "))
y_c = float(input("y_c = "))

#8. Вычислить длины сторон треугольника.
c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)

#9. Проверить, существует ли треугольник, построенный по заданным точкам, если нет - выдать сообщение пользователю.
if a + b <= c or b + c <= a or a + c <= b:
    print("error")

#10. В противном случае вычислить площадь, периметр, величины углов.
else:
    radius_in_around = compute_radius_in_around(a, b, c)
    radius_desc_around = compute_radius_desc_around(a, b, c)
    len_median = compute_len_median(a, b, c)

#11.Вывести результаты вычисления на экран, округлив их до 3 - х знаков после запятой.
    print(round(radius_in_around, 4), round(radius_desc_around, 4), round(len_median, 4))
