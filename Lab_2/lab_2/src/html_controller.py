import os
import pandas as pd
from lab_1 import FeatureWorkerFactory

class HtmlController:
    path = "data_VTm_126_lab_2.html"
    
    def __init__(self):
        if not os.path.exists(self.path):
            wf=FeatureWorkerFactory()
            self.save(wf.df)
            

    def load(self):
        result=FeatureWorkerFactory()
        try:
            tables = pd.read_html(self.path, encoding="utf-8")
            result.df=tables[0]
            result.df['Дата рождения'] = pd.to_datetime(result.df['Дата рождения'])

        except ValueError as e:
            print(e)

        return result

    def save(self,df):
        df.to_html(self.path, index=False) 
