Ocenki = input("Введите оценки через пробел: ")
five = Ocenki.count("5")
SumOc = Ocenki.count("5")+Ocenki.count("4")+Ocenki.count("3")+Ocenki.count("2")
print("Процент пятёрок: "+ str(five/SumOc*100))