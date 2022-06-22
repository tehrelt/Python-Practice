circle = {'radius': 0, 'x': 0, 'y': 0}
incircle = {'radius': 0, 'x': 0, 'y': 0}

# Ввод координатов центра первого круга

print('Введите координаты центра первого круга:')
circle['x'] = int(input('x = '))
circle['y'] = int(input('y = '))
circle['radius'] = int(input('radius = '))

# Ввод координатов центра второго круга

print('Введите координаты центра второго круга:')
incircle['x'] = int(input('x = '))
incircle['y'] = int(input('y = '))
incircle['radius'] = int(input('radius = '))

deltaX = circle['x'] - incircle['x']
deltaY = circle['y'] - incircle['y']

if incircle['radius'] < circle['radius']:
    if deltaX < circle['radius'] and deltaY < circle['radius']:
        print('Второй круг внутри первого')