import random
#функция исключаящая ввод любого символа кроме цифр

def exception_char():
    while True:
        try:
            user_number = int(input('Пожалуйста введите вашe число:'))
            user_number=str(user_number)
            return user_number
        except ValueError:
            print("Ошибка:В вашем числе есть недопустимые символы\n")

def entering_number() :
    user_number=exception_char()
    user_number = str(user_number)
    check_number(user_number)


    if check_number(user_number)==404 :
        while check_number(user_number)==404 :
            print("В вашем числе есть повторяющиеся знаки или число состоит менее или более чем из 4 символом\n")
            user_number = exception_char()
            user_number = str(user_number)

    return user_number

#функция проверки числа на вшивость
def check_number(num):
    size = len(num)
    if size != 4 or num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
       return 404



#функция ставок и её проверки
def stavka(spin) :

    stavka=int(exception_char())
    max_stavka=spin/2

    if stavka==1 :
        print(" ")
    else :
        while stavka<1 or stavka>max_stavka :
            print("Ошибка,ваша ставка не подходит\n")
            stavka=int(exception_char())
            if stavka==1 :
                break
    print("Спасибо,ваша ставка принята\n")
    return stavka


#функия рандомного числа и изменение функции проверки под рандомное число
def random_number() :
    r_num=random.randint(1000,9999)
    r_num=str(r_num)

    check_number(r_num)

    if check_number(r_num)==404 :
        while check_number(r_num)==404 :
            r_num = random.randint(1000, 9999)
            r_num = str(r_num)

    return r_num


#функция подсчета топоров и тузов
def Ace_Axe(num, random_str):
    axe = 0
    ace=0

    for char_one_num in range(4):
        if random_str[char_one_num] == num[char_one_num]:
            axe = axe + 1  
        for char_two_num in range(4):
            if random_str[char_one_num] == num[char_two_num]:
                ace = ace + 1

    if axe > 1:
        print('Вы имеете' + ' ' + str(axe) + ' ' + 'Топора')
    elif axe == 0:
        print('Вы не имеете Топоров')
    else:
        print('Вы имеете' + ' ' + str(axe) + ' ' + 'Топор')


    ace = ace - axe
    if ace>1 :
        print('Вы имеете' + ' ' + str(ace) + ' ' + 'Туза')
    elif ace==0 :
        print('Вы не имеете Тузов')
    else :
        print('Вы имеете' + ' ' + str(ace) + ' ' + 'Туз')


    return axe


#функия обьединяющая два неразрывных блока ,ввода числа и подсчета тузов и топоров
def couting_Axe_Ace(r_num) :
    print("Введите число для отгадвания:")
    num=entering_number()
    ace_axe=Ace_Axe(num,r_num)
    return ace_axe


#функция самой игры
def Game(spinkoins,stavka) :
    #рандом число
    r_num=random_number()

    #вызов игры
    axe=couting_Axe_Ace(r_num)
    print("У вас осталось 7 попыток \n")
    attempt = 1
    # условие цикличности
    if axe == 4:
        print(" ")
    else:
        while axe != 4:
            axe = couting_Axe_Ace(r_num)
            attempt = attempt + 1
            num_of_attempt = 8 - attempt
            if num_of_attempt>=5 :
                print("У вас осталось" + ' ' + str(num_of_attempt) + " попыток")
                print(" ")
            elif 1<num_of_attempt<5:
                print("У вас осталось" + ' ' + str(num_of_attempt) + " попытки")
                print(" ")
            elif num_of_attempt==1 :
                print("У вас осталось" + ' ' + str(num_of_attempt) + " попытка")
                print(" ")
            else:
                print("Игра окончена\n ")
            if attempt == 8:
                break


    if axe == 4:
        print("Поздравляем,вы угадали наше число")
    else:
        print("Простите,вы проиграли")

    if attempt <= 5:
        win = stavka * 3
    elif attempt == 6:
        win = stavka * 2
    elif attempt == 7:
        win = stavka * 0.5
    else:
        win = 0
    win = float(win)
    spinkoins = int(spinkoins + win)
    return spinkoins
