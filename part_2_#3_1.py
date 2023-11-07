# Задача 3_1
# Постройте график функции, описывающей численность населения на интервале [a, b]
# Для вычисления и прогноза численности населения Земли С. П. Капица предложил следующую формулу


import matplotlib.pyplot as plt

import math

def compute_population(t):
   #вычислить численность населения для года t по формуле
    N = (172 / 45) * ((math.pi / 2) - math.atan((2000 - t) / 45))
    return N

a = int(input())
b = int(input())
n = 100
h = (b-a)/(n-1)

x_list = [a + h * i for i in range(n)]
f_list = [compute_population(x) for x in x_list]

line = plt.plot(x_list, f_list)

plt.setp(line, color = "red", linewidth = 2)

plt.gca().spines["left"].set_position("center")
plt.gca().spines["bottom"].set_position("center")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.grid()

plt.show()

