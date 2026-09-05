import datetime as DT
import numpy as NP
import pandas as PN
from matplotlib import pyplot as PLT
def rec_create(index):
    name = input("Введите ФИО сотрудника: ")
    date_str = input("Введите дату рождения (dd/mm/yyyy): ")
    date_b = DT.datetime.strptime(date_str, '%d/%m/%Y').date()
    ch_num = int(input("Зарплата: "))
    data = [{'Индекс': index, 'ФИО': name, 'Дата рождения': date_b, 'Зарплата': ch_num }]
    df = PN.DataFrame(data)
    return df
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

    index = 0
    emp_list = PN.DataFrame()

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
            index = index+1
            rec = rec_create(index)
            emp_list = emp_list._append(rec)

        if task_number == '4':
            print(emp_list)

        if task_number == '6':
            plot_salary(emp_list['Зарплата'].to_numpy())

        if task_number == '7':
            break
