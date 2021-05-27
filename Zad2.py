from numpy import *
from pandas import *
from matplotlib.pyplot import *
import xlrd
import openpyxl
from math import *

x = np.arange(-100, 100, 0.1)
subplot(3, 1, 1)
plot(x, (-4)*x**2+(6*x/2)+20, 'ro', label='(-4)*x**2+(6*x/2)+20')
axis([-2, 4, -25, 25])
legend(loc='lower center')
grid()
title('Pierwszy wykres')


subplot(3, 1, 2)
plot(x, np.tan(x)-5, label='tan(x)-5')
axis([-2, 6, -40, 80])
legend(loc='lower left')
grid()
title('Drugi wykres')

subplot(3, 1, 3)
plot(x, (-4)*x**2+(6*x/2)+20, 'ro', label='(-4)*x**2+(6*x/2)+20')
plot(x, np.tan(x)-5, label='tan(x)-5')
axis([-2, 6, -100, 100])
title('Trzeci wykres')
legend(loc='upper left')
grid()
show()