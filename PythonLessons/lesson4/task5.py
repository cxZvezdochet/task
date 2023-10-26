cost = int(input())
while cost!=0:
    sales = int(input())
    cost = cost - sales
    print(cost)
    if cost < 0:
        cost = 0
