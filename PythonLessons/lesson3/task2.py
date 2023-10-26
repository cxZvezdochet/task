sum = float(input('Введите сумму к оплате: '))
time = int(input('Введите текущий час: '))
if time >= 10 and time <= 12:
    print(sum/2) #у меня флешбеки с Егэ
elif time >=20 and time <= 22:
    print(sum/4)
else:
    print(sum)