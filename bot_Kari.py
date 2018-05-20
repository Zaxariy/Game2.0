 # Game2.0
import vk_api
import time
# для исползования игры в системе должны находится фаил Fus_Def
from Fus_Def
import exception_char,check_number,stavka,random_number,Ace_Axe,couting_Axe_Ace,Game,entering_numberfrom Fus_Def

vk=vk_api.VkApi(token='c7d1e7566a5ec805dbb2ff7f7c4606b3edbf9b0da55d3c87042cd6ad9b192c4c7347b9ed4885e9ab9947e')
vk.auth_token()
otvet={'out': 0,'count': 140,'time_offset': 40} #что мы смогли отвечать пользователю на сообщению 
vk.otvet=('messages.get', otvet)
def write_msg(user_id, s):
  vk.method('messages.send', {'user_id':user_id,'message':s}) #для отправления конкретному пользователю с конкретным сообщением

while True:
    pole=vk.otvet=('messages.get', otvet)
    if pole ['items']:
        otvet ['last_message_id']=pole ['items'][0]['id']
    for item in pole['items']:
        if pole['items'][0]['body'] == 'Привет':
           write_msg(item['user_id'], 'Здравствуй! Хочешь сыграть в Казино 777? Если да, то нажми на Y, если нет - N')
        elif pole['items'][0]['body'] == 'Y':   
           write_msg(item['user_id'], 'Добро пожаловать в игру Топоры и Тузы 2.0. Правила игры: Игра загадывает четырех значное число,Игрок должен отгадать это число за как можно меньшое количество попыток. Цифра вашего числа называется Топором ,если в загаданном машиной числе в том же месте стоит та же цифра. Цифра вашего числа называется Тузом ,если в загаданном числе есть таже цифра,но она стоит в другом месте. Изначально вам дается 10 спинкоинов,минимальная ставка 1,максимальная половина вашего счета. При угаданном числе меньше чем за 8 попыток вам будет начисле выйграш,в противном же случаи вы потеряете часть ваших спинкоинов,а именно вашу ставку. Приятного время провождения')
           spinkoins = 10
           write_msg(item['user_id'], 'Введите вашу ставку')
           stavka_game =stavka(spinkoins)
           spinkoins_game = spinkoins - stavka_game
        
           spinkoins_game=Game(spinkoins_game,stavka_game)
           write_msg(item['user_id'], 'Ваш текущий счет:'+str(spinkoins_game))

           if spinkoins_game>0 :
             while spinkoins_game>0 :
                while True:
                   write_msg(item['user_id'], 'Желаете сыграть еще?:введите yes или no')
                   if pole['items'][0]['body'] == 'yes' or pole['items'][0]['body'] ==  'no':
                       break
                   if pole['items'][0]['body'] == 'yes':
                       write_msg(item['user_id'], 'Введите вашу ставку')
                       stavka_game =stavka(spinkoins_game)
                       spinkoins_game = spinkoins_game - stavka_game
                       spinkoins_game= Game(spinkoins_game,stavka_game)
                       write_msg(item['user_id'], 'Ваш текущий счет:'+str(spinkoins_game))
                       if spinkoins_game==0 :
                          write_msg(item['user_id'], 'Извините,вы больше не можете играть')
                          break
                   elif pole['items'][0]['body'] =='no' :
                          exit()
           else :
               write_msg(item['user_id'], 'Извините,вы больше не можете играть')
        elif pole['items'][0]['body'] == 'N':
           write_msg(item['user_id'], 'и зачем вы к нам тогда зашли? =( Если захотите поиграть обязательно напишите Y')
        else:
            write_msg(item['user_id'], 'Ваш язык мне не знаком, но все же предложу вам игру, если хотите участвовать, то нажми на Y, если нет - N')
    time.sleep(1)    
