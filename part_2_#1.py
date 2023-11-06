# Задача 1
# Вычислить значения функции
    # на интервале [a, b] построить таблицу значений, состоящую из n элементов

import math

def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

a = float(input("a = "))
b = float(input("b = "))
n = int(input("n = "))

if n < 0 or a >= b:
    print("Ошибочные входные данные")
else:
    h = (b - a) / (n - 1)

x_list = [a + i * h for i in range(n)]
f_list = [f_x(x) for x in x_list]

# вывод шапки таблицы
print("-" * 17)
print ("| %4s | %6s |" % ("x", "f(x)"))
print("-" * 17)
# вывод содержимого таблицы
for i in range(n):
    print ("| %4.1f | %6.3f |" % (x_list[i], f_list[i]))
# вывод подчеркивания
print("-" * 17)