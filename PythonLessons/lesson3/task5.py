a = input()
sum_a = 0
for i in range(len(a)):
    sum_a += int(a[i])
if int(a[-1::]) %2 == 0:
    if sum_a % 3 == 0:
        print('Да')
else:
    print('Нет')