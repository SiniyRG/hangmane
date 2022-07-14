def game_1(text, error):
    global user1
    stages = ["_________       ",
              "         |      ",
              "         |      ",
              "         0      ",
              "        /|\     ",
              "        / \     ",
              ]
    print("\nВиселица:")
    for i in range(error):
        print(stages[i])
    print(f"Слово:{text}")
    if len(stages) - error == 0:
        print("\nКонец игры.\nПервый игрок победил.")
        return 0
    elif text == user1:
        print("\nКонец игры.\nВторой игрок победил.")
        return 0
    else:
        print(f"Попыток:{len(stages)-error}\n")


user1 = input("Введите слово, которое нужно угадать:").lower()
user1_text = "_" * len(user1)
error_game = 0
while game_1(user1_text, error_game) != 0:
    user2 = input("Введите букву:").lower()
    start = 0
    if user2 in user1:
        print(f"Верно, буква {user2} встречается {user1.count(user2)} раз/а")
        while user2 in user1[start:]:
            user1_text = user1_text[:user1.find(user2, start)] + user2 + user1_text[user1.find(user2, start)+1:]
            start = user1.find(user2, start) + 1
    else:
        print("Такой буквы нет")
        error_game += 1



