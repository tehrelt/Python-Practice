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
# - метод «Изменение цеха» void ChangeDepartment (int NewDepartment).

import os

class Employee(object):
    def __init__(self, fio, number, stage, age):
        self.fio = fio
        self.number = number
        self.stage = stage
        self.age = age

    def growUp(self, age):
        self.age += age

    def show(self):
        print('ФИО: ' + self.fio)
        print('Номер: ' + self.number)
        print('Стаж: ' + self.stage)
        print('Возраст: ' + self.age)

class Turner(Employee):
    def __init__(self, fio, number, stage, age, experience, department):
        super().__init__(fio, number, stage, age)
        self.experience = experience
        self.department = department
    
    def changeDepartment(self, department):
        self.department = department
    
    def show(self):
        super().show()
        print('Опыт: ' + self.experience)
        print('Отдел: ' + self.department)

employees = []
turners = []
while True:
    print('1. Создать сотрудника')
    print('2. Создать токаря')
    print('3. Вывести информацию о сотрудниках')
    print('4. Вывести информацию о токарях')
    print('5. Удалить объект сотрудника')
    print('6. Удалить объект токаря')
    print('7. Выход')
    key = input('Введите номер действия: ')
    os.system('cls')
    match key:
        case '1':
            fio = input('Введите ФИО: ')
            number = input('Введите номер: ')
            stage = input('Введите стаж: ')
            age = input('Введите возраст: ')
            employees.append(Employee(fio, number, stage, age))
        case '2':
            fio = input('Введите ФИО: ')
            number = input('Введите номер: ')
            stage = input('Введите стаж: ')
            age = input('Введите возраст: ')
            experience = input('Введите опыт: ')
            department = input('Введите отдел: ')
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
            print('Введите номер сотрудника, которого хотите удалить: ')
            index = input('Введите номер сотрудника: ')
            toremove = employees.pop(int(index)-1)
            del toremove
        case '6':
            i = 0
            for turner in turners:
                print('\tСотрудник-Токарь #' + str(i+1))
                turner.show()
                print('')
                i += 1
            print('Введите номер сотрудника-токаря, которого хотите удалить: ')
            index = input('Введите номер сотрудника-токаря: ')
            toremove = turners.pop(int(index)-1)
            del toremove
        case '7':
            break
    print('\n')

