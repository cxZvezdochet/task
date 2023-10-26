a = ['=', '?', '*','^','$','№','@','_']
log = input()
for i in range(len(log)):
    if log[i] in a:
        print(log[i] + ' Запрещенный символ')