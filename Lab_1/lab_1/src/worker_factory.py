import pandas as PN
from .worker import Worker

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