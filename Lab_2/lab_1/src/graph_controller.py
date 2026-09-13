import numpy as NP
from matplotlib import pyplot as PLT

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