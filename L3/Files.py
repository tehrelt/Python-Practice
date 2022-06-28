# 8.    Предельно доспутимые концентрации (ПДК) загрязняющих веществ в
#       атмосферном воздухе населённых пунктов
# 
# Вещество          ПДК                                     Класс опасности
#                   Максимальная разовая    Среднесуточная
# Ксилол            0,2                     0.2             3
# Метилстирол       0,04                    0,4             3
# Нафталин          0,003                   0,003           4
# Пеницилин         0,05                    0,0025          3
# Пентан            100                     25              4
# 
# У каких веществ отношение среднесуточной ПДК к максимальной разовой
# ПДК превышает D? [вещество, среднесуточная ПДК, отношение
# максимальной разовой ПДК к среднесуточная ПДК].

import os

while True:
    print('1. Записать в файл')
    print('2. Прочитать из файла')
    print('3. У каких веществ отношение среднесуточной ПДК к максимальной разовой ПДК превышает D?')
    print('4. Выход')
    key = input('Введите номер пункта: ')
    os.system('cls')
    match key:
        case '1':
            print('Записать в файл')
            with open('file.txt', 'a', encoding='utf-8') as f:
                key = 'y'

                while key == 'y':
                    row = {}
                    row['name'] = input('Введите вещество: ')           
                    row['max_pdk'] = float(input('Введите максимальную разовую ПДК: '))      
                    row['average_pdk'] = float(input('Введите среднесуточную ПДК: '))
                    row['class_of_danger'] = int(input('Введите класс опасности: '))
                    f.write(row['name'] + ' ' + str(row['max_pdk']) + ' ' + str(row['average_pdk']) + ' ' + str(row['class_of_danger']) + '\n')
                    key = ''
                    while key != 'n' and key != 'y':
                        key = input('Добавить ещё одно вещество? (y/n): ')


        case '2':
            print('Прочитать из файла')
            with open('file.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    sub = line.split(' ')
                    print(sub[0] + '\t' + sub[1] + '\t' + sub[2] + '\t' + sub[3], sep='', end='')

                print()

        case '3':
            print('У каких веществ отношение среднесуточной ПДК к максимальной разовой ПДК превышает D?')
            with open('file.txt', 'r', encoding='utf-8') as f:
                D = float(input('Введите D: '));
                print('[вещество, среднесуточная ПДК, отношение максимальной разовой ПДК к среднесуточная ПДК]')
                for line in f:
                    sub = line.split(' ')
                    ratio = float(sub[2]) / float(sub[1])
                    if ratio > D:
                        print(sub[0] + '\t' + sub[2] + '\t' + str(ratio), sep='', end='')
                        print()

        case '4':
            print('Выход')
            break
        case default:
            print('Неверный пункт')
    print()
