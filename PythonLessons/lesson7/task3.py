"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""
newspaper = list(range(1, 76))
magazine = list(range(77, 104))
both = list(range(21, 34))


lenAll= len(newspaper + magazine)
both1 = len(both)
nothing = both1 - lenAll

all = abs(nothing + len(both))

print(all)