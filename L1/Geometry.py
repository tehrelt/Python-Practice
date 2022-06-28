def input_in_range(message, min = -300000000, max = 300000000):   # Функция для ввода числа в диапазоне
    while True:
        try:
            value = int(input(message))
            if value >= min and value <= max:
                return value
            else:
                print('Введено неверное значение')
        except ValueError:                                          # Обработка ошибки ввода
            print('Введено неверное значение')

circle = {'radius': 0, 'x': 0, 'y': 0}
incircle = {'radius': 0, 'x': 0, 'y': 0}

# Ввод параметров первого круга
print('Введите параметров первого круга:')
circle['x'] = int(input_in_range('x = '))
circle['y'] = int(input_in_range('y = '))
circle['radius'] = int(input_in_range('radius = ', 0))

# Ввод параметров второго круга
print('Введите параметров второго круга:')
incircle['x'] = int(input_in_range('x = '))
incircle['y'] = int(input_in_range('y = '))
incircle['radius'] = int(input_in_range('radius = ', 0))

deltaX = circle['x'] - incircle['x']
deltaY = circle['y'] - incircle['y']

if incircle['radius'] < circle['radius']:
    if deltaX < circle['radius'] and deltaY < circle['radius']:     # Проверка на пересечение кругов 
        print('Второй круг внутри первого')
    else:
        print('Второй круг не внутри первого')