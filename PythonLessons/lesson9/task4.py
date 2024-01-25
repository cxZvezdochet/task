"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def calculate(*args):
    average = sum(args) / len(args)
    greater_than_average = [x for x in args if x > average]
    return average, greater_than_average

result = calculate(1, 2, 3, 4, 5, 6, 7)
print(result)