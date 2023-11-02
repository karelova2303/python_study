# Задача # 2. Вычисление индекса массы тела и его интерпретация

# пользователь, кроме имени, вводил свой возраст, рост и вес.
age = int(input())
height = float(input())
weight = float(input())

# проверка введенных данных на корректность
if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)
    if age < 45:
        if bmi < 18.5:
            description = "недостаточной массой тела."
        elif bmi < 25:
            description = "нормальной массой тела."
        elif bmi < 30:
            description = "избыточной массой тела."
        else:
            description = "ожирением."
        print("bmi=", bmi, "Вы относитесь к группе людей с", description)
    else:
        if bmi < 22:
            description = "недостаточной массой тела."
        elif bmi < 27:
            description = "нормальной массой тела."
        elif bmi < 32:
            description = "избыточной массой тела."
        else:
            description = "ожирением."
        print("bmi=", bmi, "Вы относитесь к группе людей с", description)