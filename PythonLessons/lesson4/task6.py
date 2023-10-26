cost = int(input())
if cost %2 == 0:
    while cost != 0:
        if cost %2 == 0:
            cost//2
        else:
            print("К оплате: " + str(cost))
else:
    print(" оплате: " + str(cost*0.85))