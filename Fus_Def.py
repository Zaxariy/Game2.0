#функция исключаящая ввод символов
def only_number():
    while True:
        try:
            num = int(input('Пожалуйста введите вашe число:'))
            num=str(num)
            return num
        except ValueError:
            print("Ошибка:В вашем числе есть недопустимые символы")



#функция проверки числа на вшивость
def proverka(num):
    size = len(num)
    if size != 4 or num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
        while size != 4 or num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
            print("Ошибка:В вашем числе есть повторяющиеся знаки или в нем больше 4 символов ")
            num = only_number()
            size = len(num)
    return num



#функция ставок и её проверки
def stavka(spin) :
    from Fus_Def import only_number

    stavka=int(only_number())
    max_stavka=spin/2

    if stavka==1 :
        print("Спасибо,ваша ставка принята")
    else :
        while stavka<1 or stavka>max_stavka :
            print("Ошибка,ваша ставка не подходит")
            stavka=int(only_number())
            if stavka==1 :
                break
    return stavka


#функия рандомного числа и изменение функции проверки под рандомное число
def random_number() :
    import random

    r_num=random.randint(1000,9999)
    r_num=str(r_num)


    def proverka(num):
        size = len(num)
        if size != 4 or num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
            while size != 4 or num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
                num = random.randint(1000,9999)
                num=str(num)
                size = len(num)
        return num

    r_num=proverka(r_num)
    return r_num


#функция подсчета топоров и тузов
def Ace_Axe(num, random_str):

    schet = 0
    axe = 0

    for schet in range(4):
        if random_str[schet] == num[schet]:
            axe = axe + 1
        else:
            schet = schet + 1
    if axe > 1:
        print('Вы имеете' + ' ' + str(axe) + ' ' + 'Топора')
    elif axe == 0:
        print('Вы не имеете Топоров')
    else:
        print('Вы имеете' + ' ' + str(axe) + ' ' + 'Топор')

    schet_two = 0
    schet_tree = 0
    ace = 0
    # конец
    for schet_two in range(4):
        for schet_tree in range(4):
            if random_str[schet_two] == num[schet_tree]:
                ace = ace + 1
            else:
                schet_tree = schet_tree + 1



    ace = ace - axe
    if ace>1 :
        print('Вы имеете' + ' ' + str(ace) + ' ' + 'Туза')
    elif ace==0 :
        print('Вы не имеете Тузов')
    else :
        print('Вы имеете' + ' ' + str(ace) + ' ' + 'Туз')


    return axe


#функия обьединяющая два неразрывных блока ,ввода числа и подсчета тузов и топоров
def one_open_game(r_num) :
    print("Введите число для отгадвания:")
    num=proverka(only_number())
    ace_axe=Ace_Axe(num,r_num)
    return ace_axe


#функция самой игры
def Game(spinkoins,stavka) :
    #рандом число
    r_num=random_number()


    #вызов игры
    axe=one_open_game(r_num)
    print("У вас осталось 9 попыток \n")
    poputka = 1
    # условие цикличности
    if axe == 4:
        print(" ")
    else:
        while axe != 4:
            axe = one_open_game(r_num)
            poputka = poputka + 1
            kol_poput = 10 - poputka
            if kol_poput!=0 :
                print("У вас осталось" + ' ' + str(kol_poput) + " попыток")
                print(" ")
            else :
                print("Игра окончена\n")

            if poputka == 10:
                break


    if axe == 4:
        print("Поздравляем,вы угадали наше число")
    else:
        print("Простите,вы проиграли")

    if poputka <= 6:
        win = stavka * 2 + stavka
    elif poputka == 7:
        win = stavka * 1 + stavka
    elif poputka == 8:
        win = stavka * 0.6 + stavka
    elif poputka == 9:
        win = stavka * 0.2 + stavka
    else:
        win = 0
    win = float(win)
    spinkoins = int(spinkoins + win)
    #print("Ваш текущий счет:" + " " + str(spinkoins))
    return spinkoins
