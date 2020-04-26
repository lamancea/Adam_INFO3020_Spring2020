import matplotlib.pyplot as plt
import pandas as pd

def salestrend(food):
    filename = "assign11-1-catering_sale_all.xls"
    data = pd.read_excel(filename, header=0)
    x=data[food].to_list()
    y=data['sale date'].to_list()
    plt.xlabel('Date')
    plt.ylabel('Sales($)')
    plt.title(food)
    plt.xticks(rotation=45)
    plt.plot(y,x)
    plt.show()


salestrend('ribs')
