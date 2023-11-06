# Задача 8
# Напишите программу, которая для целого числа k (от 1 до 99) напечатает фразу «k рублей»,
# учитывая при этом, что при некоторых значениях слово «рублей» заменяется на «рубль» или «рубля».
# Например: 2 рубля, 13 рублей, 41 рубль.
# Если введено значение вне интервала от 1 до 99, то вывести "ошибка".
# Входные данные: # сумма в рублях (целое число).
# Выходные данные: # число и слово рубль  в нужном падеже (строка текста) или ошибка.

# Ввод данных
k = int(input('Введите число: '))

rub_1 = ' рубль'
rub_2 = ' рубля'
rub_3 = ' рублей'
remain = k  % 10

# Условие проверки корректности введенных данных
if k <= 0 or k > 99:
    print('ошибка')
elif (remain == 1) and k != 11:
    print(k, rub_1)
elif (remain == 2 or remain == 3 or remain == 4) and (k < 11 or k > 15):
    print(k, rub_2)
else:
    print(k, rub_3)




