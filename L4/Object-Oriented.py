# Вариант 8
# Создать класс Employee, содержащий в себе следующие элементы:
# - поле «ФИО» char * FIO;
# - поле «Табельный номер» int Number;
# - поле «Возраст» int Age;
# - поле «Стаж» int Stage;
# - конструктор с параметрами Employee(char * FIO, int Number, int Stage,
# int Age).
# - метод «увеличить возраст»;
# Унаследовать от класса Employee класс Turner (Токарь), содержащий в
# себе элементы:
# - поле «Разряд» int Experience;
# - поле «Номер цеха» int Department;
# - конструктор с параметрами Turner(char * FIO, int Number, int Stage, int
# Age, int Department, int Experience);
# - метод «Изменение цеха» void change_department (int NewDepartment).

import os
from classes import Employee, Turner

employees = []
turners = []

def input_in_range(message, min = 0, max = 300000000):
    while True:
        try:
            value = int(input(message))
            if value >= min and value <= max:
                return value
            else:
                print('Введено неверное значение')
        except ValueError:
            print('Введено неверное значение')

while True:
    print('1. Создать сотрудника')
    print('2. Создать токаря')
    print('3. Вывести информацию о сотрудниках')
    print('4. Вывести информацию о токарях')
    print('5. Удалить объект сотрудника')
    print('6. Удалить объект токаря')
    print('7. Увеличить возраст сотрудника')
    print('8. Поменять отдел токаря')
    print('9. Выход')
    key = input('Введите номер действия: ')
    os.system('cls')
    match key:
        case '1':
            fio = input('Введите ФИО: ')
            number = input_in_range('Введите номер: ')
            stage = input_in_range('Введите стаж: ')
            age = input_in_range('Введите возраст: ')
            employees.append(Employee(fio, number, stage, age))
        case '2':
            fio = input('Введите ФИО: ')
            number = input_in_range('Введите номер: ')
            stage = input_in_range('Введите стаж: ')
            age = input_in_range('Введите возраст: ')
            experience = input_in_range('Введите опыт: ')
            department = input_in_range('Введите отдел: ')
            turners.append(Turner(fio, number, stage, age, experience, department))
        case '3':
            i = 0
            for employee in employees:
                print('\tСотрудник #' + str(i+1))
                employee.show()
                print('')
                i += 1
        case '4':
            i = 0
            for turner in turners:
                print('\tСотрудник-Токарь #' + str(i+1))
                turner.show()
                print('')
                i += 1
        case '5':
            i = 0
            for employee in employees:
                print('\tСотрудник #' + str(i+1))
                employee.show()
                print('')
                i += 1
            index = input_in_range('Введите номер сотрудника, которого хотите удалить: ', 0, i)
            toremove = employees.pop(int(index)-1)
            del toremove
        case '6':
            i = 0
            for turner in turners:
                print('\tСотрудник-Токарь #' + str(i+1))
                turner.show()
                print('')
                i += 1
            index = input_in_range('Введите номер сотрудника, которого хотите удалить: ', 0, i)
            toremove = turners.pop(int(index)-1)
            del toremove
        case '7':
            i = 0
            for employee in employees:
                print('\tСотрудник #' + str(i+1))
                employee.show()
                print('')
                i += 1
            index = input_in_range('Введите номер сотрудника, возраст которого хотите увеличить: ', 0, i)
            age = input_in_range('На сколько лет увеличить возраст: ')
            employees[int(index)-1].grow_up(age)
        case '8':
            i = 0
            for turner in turners:
                print('\tСотрудник-Токарь #' + str(i+1))
                turner.show()
                print('')
                i += 1
            index = input_in_range('Введите номер сотрудника, отдел которого хотите изменить: ', 0, i)
            department = input_in_range('Введите новый отдел: ')
            turners[int(index)-1].change_department(department)
        case '9':
            break
    print('\n')