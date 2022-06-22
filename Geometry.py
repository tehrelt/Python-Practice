def inputInRange(message, min = -300000000, max = 300000000):
    while True:
        try:
            value = int(input(message))
            if value >= min and value <= max:
                return value
            else:
                print('Введено неверное значение')
        except ValueError:
            print('Введено неверное значение')

circle = {'radius': 0, 'x': 0, 'y': 0}
incircle = {'radius': 0, 'x': 0, 'y': 0}

# Ввод параметров первого круга

print('Введите параметров первого круга:')
circle['x'] = int(inputInRange('x = '))
circle['y'] = int(inputInRange('y = '))
circle['radius'] = int(inputInRange('radius = ', 0))

# Ввод параметров второго круга

print('Введите параметров второго круга:')
incircle['x'] = int(inputInRange('x = '))
incircle['y'] = int(inputInRange('y = '))
incircle['radius'] = int(inputInRange('radius = ', 0))

deltaX = circle['x'] - incircle['x']
deltaY = circle['y'] - incircle['y']

if incircle['radius'] < circle['radius']:
    if deltaX < circle['radius'] and deltaY < circle['radius']:
        print('Второй круг внутри первого')