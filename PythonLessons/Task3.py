"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
track = {}
begin = input()
while begin.lower != 'off':
    begin1 = input('Введите место в чарте:  ')
    if begin1.lower() == 'off':
        break
    begin2 = input('Введите исполнителя:  ')
    if begin2.lower() == 'off':
        break
    begin3 = input('Введите название:  ')
    if begin3.lower() == 'off':
        break
    track[(begin1, begin2)] = begin3
    print(track)
