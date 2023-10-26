a=float(input())
b=float(input())
colors=float(input())
V=int(input())
All_percent=int(input())

S=(round(float(a*b),2))
count_litres=(round(float(S/colors),2))#да
count_litres=count_litres+(count_litres*All_percent/100)
count_jars=(count_litres//V)+1
count_no_use_litres=(round(float(count_jars*V-count_litres),2))

print(S)
print(round(count_litres,2))
print(int(count_jars))
print(count_no_use_litres)
