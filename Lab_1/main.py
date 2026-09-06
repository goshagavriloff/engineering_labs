import datetime as DT
import numpy as NP
import pandas as PN
from matplotlib import pyplot as PLT

class Worker:
    def __init__(self):
        self.__name = input("Введите ФИО сотрудника: ")
        self.__date_str = input("Введите дату рождения (dd/mm/yyyy): ")
        self.__ch_num=int(input("Зарплата: "))
        self.__date_b = DT.datetime.strptime(self.__date_str, '%d/%m/%Y').date()
        self.data = {'ФИО': self.__name, 'Дата рождения': self.__date_b, 'Зарплата': self.__ch_num }

class WorkerFactory:
    def __init__(self):
        self.df = PN.DataFrame(columns=['ФИО', 'Дата рождения','Зарплата'])

    def create(self):
        w= Worker()
        self.df.loc[len(self.df)] = w.data
        self.df.index = PN.RangeIndex(start=1,stop=1+len(self.df), name='Индекс')

    def __str__(self):
        return self.df.to_string()


def plot_salary(salary_array):
    groups = NP.zeros(6)
    for i in salary_array:
        if i < 25000:
            groups[0] = groups[0]+1
        elif i < 50000:
            groups[1] = groups[1]+1
        elif i < 75000:
            groups[2] = groups[2]+1
        elif i < 100000:
            groups[3] = groups[3]+1
        elif i < 125000:
            groups[4] = groups[4]+1
        else:
            groups[5] = groups[5]+1

    PLT.bar(['<25000', '25000:50000', '50000:75000', '75000:100000', '100000:125000', '>125000'], groups)
    PLT.show()


if __name__ == '__main__':

    factory=WorkerFactory()
    name = 'true'
    while True:
        print("Выберите действие из списка:")
        print("1) Добавление данных о сотруднике")
        print("2) Удаление данных о сотруднике")
        print("3) Изменение данных о сотруднике")
        print("4) Вывод списка сотрудников")
        print("5) Вывод списка сотрудников младше заданного возраста")
        print("6) Вывод диаграммы распределения зарплат")

        print("8) Завершение программы")
        task_number = input("Введите номер команды: ")

        if task_number == '1':
            factory.create()
        if task_number == '4':
            print(factory)

        if task_number == '6':
            plot_salary(factory.df['Зарплата'].to_numpy())

        if task_number == '8':
            break
