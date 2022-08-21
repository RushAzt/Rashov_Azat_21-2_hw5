from random import randint
import os
from envparse import env
env.read_envfile('settings.env')
money = os.getenv('MY_MONEY')

slot = randint(1,2)
def game():
    global money
    print('~~~Добро пожаловать в казино MAIN!\n'
          'Попытайте свою удачи в этом казино.\n'
          'Eсли угадайте то ваша ставка возвысится в 5 раз,\n'
          'посмотрим ка как у вас с удачей поехали!~~~')
    try:
        while 1:
            print(f'Ваш нынешний баланс: {money}')
            com = input('Сделайте свой выбор\n1 Играть \n2 Выйти\n')
            if com == '1':
                insrt = int(input('Выберите слот: '))
                stav = int(input('Сколько хотите поставить: '))
                if insrt == slot and stav <= money:
                    money += (stav*5)
                    print(f'Вы угодали!')
                elif slot != insrt and stav <= money:
                    if money > 0 and stav <= money:
                        money -= stav
                        print(f'Вы не угодали!  было число: {slot}')
                elif money == 0:
                    print('Вы проиграли все свои денги')
                    continue
                elif stav > money:
                    print('У вас не хватает средств!')
            elif com == '2':
                if money < 1000:
                    print('Вы в проиграше')
                    print('Игра окончена')
                    print(f'Ваша баланс {money}')
                    break
                elif money > 1000:
                    print('ВЫ в выйграше')
                    print('Игра окончена')
                    print(f'Ваш баланс {money}')
                    break
            else:
                print('Нет такой меню!')
    except TypeError:
        print('Что-то пошлшо не так!')
    except ValueError:
        print('Пишите только числа!')
    except Exception:
        print('Что-то пошло не так')

