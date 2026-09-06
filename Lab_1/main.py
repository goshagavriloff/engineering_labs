import datetime as DT
import numpy as NP
import pandas as PN
from matplotlib import pyplot as PLT
from functools import wraps
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Worker:
    name: str
    date_b: DT.date
    ch_num: int
    isRinged:bool

    data: dict = field(init=False)

    def __post_init__(self):
        self.data = {'ФИО': self.name, 'Дата рождения': self.date_b, 'Зарплата': self.ch_num,'Женат/замужем':self.isRinged }
    

    @classmethod
    def from_input(cls,old_data=None):
        name = input("Введите ФИО сотрудника: ") or (None if old_data is None else old_data.get("ФИО")  )
        date_str = input("Введите дату рождения (dd/mm/yyyy): ") or (None if old_data is None else old_data.get("Дата рождения").strftime('%d/%m/%Y')  )
        ch_num=(input("Зарплата: ")) or (0 if old_data is None else old_data.get("Зарплата")  )
        ring_str = (input("Семейное положение (женат/замужем/холост): ").strip().lower()) or (False if old_data is None else str(old_data.get("Женат/замужем"))  )

        date_b = DT.datetime.strptime(date_str, '%d/%m/%Y').date()
        isRinged = ring_str in ['женат', 'замужем', 'true', '1','True']


        return cls(name=name,date_b=date_b,ch_num=int(ch_num),isRinged=isRinged)

    
class WorkerFactory:
    def __init__(self):
        self.df = PN.DataFrame(columns=['ФИО', 'Дата рождения','Зарплата','Женат/замужем'])

    def create(self,w:Worker=None):
        w= Worker.from_input() if w is None else w
        new_row=PN.DataFrame([w.data])
        self.df = PN.concat([self.df, new_row], ignore_index=True)
        self.df.index = PN.RangeIndex(start=1,stop=1+len(self.df), name='Индекс')
        self.df['Дата рождения'] = PN.to_datetime(self.df['Дата рождения'])


    def __str__(self):
        return self.df.to_string()


class Decorator:
    @staticmethod
    def inputId(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result=None
            value=(input("Введите id:")).lstrip()

            if value.isdigit():
                kwargs['id'] = int(value)
                result = func(self, *args, **kwargs) 
            else:
                print("Неправильный формат id")
            return result
        return wrapper


class FeatureWorkerFactory(WorkerFactory):
    def __init__(self):
        super().__init__()

    @Decorator.inputId
    def delete(self,id:int=None):
        self.df.drop(index=id, inplace=True, errors='ignore')

    @Decorator.inputId
    def update(self,id:int=None):
        old_data=self.df.loc[id]
        print("Введите новые данные; для сохранения текущих значений просто нажмите Enter ")
        w=Worker.from_input(old_data)
        new_data=w.data
        
        result = {k: new_data[k] if new_data[k] not in (None, '') else old_data.get(k) for k in new_data}
        self.df.loc[id]=result




class WorkerController:
    def __init__(self):
        self.__factory= FeatureWorkerFactory()
        self.__graph= GraphController()
        self.active=True
    
    def create(self):
        """Добавление данных о сотруднике"""
        self.__factory.create()

    def delete(self):
        """Удаление данных о сотруднике"""
        self.__factory.delete()

    def update(self):
        """Изменение данных о сотруднике"""
        self.__factory.update()

    def selectAll(self):
        """Вывод списка сотрудников"""
        result=self.__factory
        print(result)
        

    def selectByQuery(self):
        """Вывод списка сотрудников младше заданного возраста"""
        df=self.__factory.df
        now = PN.Timestamp.now()

        query=int(input("Введите возраст"))

        result = df[(now.year - df["Дата рождения"].dt.year) < query]
        print(result)
        

    def plotBar(self):
        """Вывод диаграммы распределения зарплат"""
        data=self.__factory.df['Зарплата'].to_numpy()
        self.__graph.plot_salary(data)

    def plotCircle(self):
        """Создание круговой диаграммы, содержащей информацию о количестве сотрудников в браке и вне брака. """
        data=self.__factory.df['Женат/замужем'].to_numpy()
        self.__graph.plot_circle(data)

    def exit(self):
        """Завершение программы"""
        self.active=False

    def print_task_list(self):
        print(f""" Выберите действие из списка:
        1) {self.create.__doc__}
        2) {self.delete.__doc__}
        3) {self.update.__doc__}
        4) {self.selectAll.__doc__}
        5) {self.selectByQuery.__doc__}
        6) {self.plotBar.__doc__}
        7) {self.plotCircle.__doc__}
        8) {self.exit.__doc__}
        """)
        

        
class GraphController:
    def plot_salary(self,salary_array):
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

    def plot_circle(self,ring_array):
        labels = ["Холост", "Женат/Замужем"]
        groups = NP.zeros(2)
        for el in ring_array:
            i=0 if el is True else 1
            groups[i]+=1
        PLT.pie(groups,labels=labels,autopct='%1.1f%%')
        PLT.show()


if __name__ == '__main__':

    c=WorkerController()
    name = 'true'
    while c.active:
        c.print_task_list()
        task_number = input("Введите номер команды: ")

        match task_number:
            case '1':
                c.create()
            case '2':
                c.delete()
            case '3':
                c.update()
            case '4':
                c.selectAll()
            case '5':
                c.selectByQuery()
            case '6':
                c.plotBar()
            case '7':
                c.plotCircle()
            case '8':
                c.exit()
            case _:
                print(f"Неизвестный номер команды: {task_number}")
