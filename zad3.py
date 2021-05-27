from numpy import *
from pandas import *
from matplotlib.pyplot import *
import xlrd
import openpyxl
from math import *

a = read_csv('cars.csv', header=0, sep=';')
print(a)
b = a[(a['Model year'] > 71) & (a['Model year'] < 78)].groupby(['Model year']).agg({'Model year': ['count']})
wykres = b.plot.bar()
xticks(rotation=0)
ylabel("Ilość aut")
xlabel("Roczniki aut")
legend(loc=False)
title('Tytuł')
show()

