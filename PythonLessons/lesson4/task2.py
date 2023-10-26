begin = input()
while begin.lower!='off':
    begin = input('Введите game:  ')
    print(begin)
    if begin.lower() == 'game':
        print("Угадай число")
        for i in range(3):
            begin = int(input())
            if begin == 5:
                print("Вы выйграли")
        else:
            print('Попробуйте ещё раз')


