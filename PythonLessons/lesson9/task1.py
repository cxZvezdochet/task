"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
def task(a,b,n):
    if a is not None:
        print(f"a:{a}")
    if b is not None:
        print(f"b:{b}")
    if n is not None:
        print(f"n:{n}")
task(1,2,None)