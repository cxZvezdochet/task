a = []
b =input()
a.extend(b)
print(a)
if len(a)==1:
    print("Нет")
else:
    for i in range(len(a)-1):
        if int(a[i+1])-int(a[i])==1:
            print("Да")
            break
        else:
            print("Нет")
            break