num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = int(num1 + num2 + num3)
if num1>num2>num3:
    print('Акция! К оплате:', sum/3)
elif num3>num2>num1:
    print('Акция! К оплате:', sum/2)
else:
    print("К оплате:", sum)