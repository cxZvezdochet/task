games=[]
while True:
    game = input("Введите название игры: ")
    if game == "0":
        break
    elif game in games:
        print("Игра уже добавлена.")
    else:
        games.append(game)
    games.sort()
    print("Список имеющихся игр", games)




