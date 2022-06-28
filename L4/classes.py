class Employee(object):
    fio : str
    number : int
    stage : int
    age : int

    def __init__(self, fio : str, number : int, stage : int, age : int):
        self.fio = fio
        self.number = number
        self.stage = stage
        self.age = age

    def grow_up(self, age : int):
        self.age += age

    def show(self):
        print('ФИО: ' + self.fio)
        print('Номер: ' + str(self.number))
        print('Стаж: ' + str(self.stage))
        print('Возраст: ' + str(self.age))

class Turner(Employee):
    experience : int
    department : int

    def __init__(self, fio : str, number : int, stage : int, age : int, experience : int, department : int):
        super().__init__(fio, number, stage, age)
        self.experience = experience
        self.department = department
    
    def change_department(self, department):
        self.department = department
    
    def show(self):
        super().show()
        print('Опыт: ' + str(self.experience))
        print('Отдел: ' + str(self.department))
