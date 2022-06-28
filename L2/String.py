# 8. Найти номера (местоположение) всех точек в строке.

string = input('Введите строку: ')
res = ''
length = len(string)
current = 0

print('Длина строки:', length)

while current < length and current != -1:
    current = string.find('.', current, length) + 1
    res += str(current)
    res += ', '

res = res[:-2] # Удаляем последнюю запятую

print(res)
