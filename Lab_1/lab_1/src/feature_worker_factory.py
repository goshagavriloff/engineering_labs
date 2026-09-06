from .worker_factory import WorkerFactory
from .decorator import Decorator
from .worker import Worker

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