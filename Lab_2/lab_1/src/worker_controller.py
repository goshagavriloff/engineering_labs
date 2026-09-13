import pandas as PN
from .feature_worker_factory import FeatureWorkerFactory
from .graph_controller import GraphController

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