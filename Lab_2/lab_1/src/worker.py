import datetime as DT
from dataclasses import dataclass, field

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

        date_b = DT.datetime.strptime(date_str, '%d/%m/%Y')
        isRinged = ring_str in ['женат', 'замужем', 'true', '1','True']


        return cls(name=name,date_b=date_b,ch_num=int(ch_num),isRinged=isRinged)