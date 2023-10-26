category = input('Введите категорию товара: ').lower()
if category == 'продукты':
    price = int(input('Введите цену: '))
    if price <= 100:
        print('Попробуйте нашу выпечку!')
    elif 500 > price >= 100:
        print('Как насчёт орехов в шоколаде?')
    else:
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома!')