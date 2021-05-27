#Zestaw B

from numpy import *
from pandas import *
from matplotlib.pyplot import *
import xlrd
import openpyxl

#Zad 1

a = read_csv('cars.csv', decimal='.', sep=';')
print(a)

b = a[a['Horsepower'] > 105]
print(b)

c = a.groupby(['Model year']).agg({'Model year':['count']})
print(c)

wykres = c.plot.pie(subplots=True, autopct='%.2f %%')
title("Tytuł")
savefig('wykres.png')
show()

