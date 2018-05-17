from Fus_Def import exception_char,check_number,stavka,random_number,Ace_Axe,couting_Axe_Ace,Game,entering_number
#оглавление
print("\t\t\tДобро пожаловать в игру Топоры и Тузы 2.0")
print("\t\t\tПравила игры ")
print("Игра загадывает четырех значное число,Игрок должен отгадать это число за как можно меньшое количество попыток")
print("Цифра вашего числа называется Топором ,если в загаданном машиной числе в том же месте стоит та же цифра")
print("Цифра вашего числа называется Тузом ,если в загаданном числе есть таже цифра,но она стоит в другом месте")
print("Изначально вам дается 10 спинкоинов,минимальная ставка 1,максимальная половина вашего счета")
print("При угаданном числе меньше чем за 8 попыток вам будет начисле выйграш,в противном же случаи вы потеряете часть ваших спинкоинов,а именно вашу ставку ")
print("\t\t\tПриятного время провождения\n")



spinkoins = 10
print("Введите вашу ставку\n")
stavka_game =stavka(spinkoins)
spinkoins_game = spinkoins - stavka_game


spinkoins_game=Game(spinkoins_game,stavka_game)
print("Ваш текущий счет:"+str(spinkoins_game))

if spinkoins_game>0 :
    while spinkoins_game>0 :
        while True:
            print("Желаете сыграть еще?:введите yes или no")
            otvet = input("Ваш ответ:")
            otvet = otvet.lower()
            otvet = otvet.rstrip()
            if otvet == 'yes' or otvet == 'no':
                break
        if otvet == 'yes':
            print("Введите вашу ставку")
            stavka_game =stavka(spinkoins_game)
            spinkoins_game = spinkoins_game - stavka_game
            spinkoins_game= Game(spinkoins_game,stavka_game)
            print("Ваш текущий счет:"+str(spinkoins_game))
            if spinkoins_game==0 :
                print("Извините,вы больше не можете играть")
                break
        elif otvet=='no' :
            exit()
else :
    print("Извините,вы больше не можете играть")





