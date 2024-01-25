"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def calculate_bmi(weight, height):
    index = weight / (height * height)
    return index

def process_bmi(index):
    if index < 18.5:
        print("Недостаточный вес")
    elif 18.5 <= index < 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")

weight = float(input("Введите свой вес в килограммах: "))
height = float(input("Введите свой рост в метрах: "))
body_mass_index = calculate_bmi(weight, height)
process_bmi(body_mass_index)