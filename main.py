import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


# Zad1
# x = np.arange(1,20,1)
# y = (1/x)
# plt.plot(x,y,label="f(x)")
# plt.ylim(0,1)
# plt.xlim(0,20)
# plt.legend()
# plt.show()

# Zad2
# x2 = np.arange(1,20,1)
# y2 = (1/x)
# plt.plot(x2,y2,":",label="f(x) = 1/x",color="red")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("wykres f(x) 1 20")
# plt.ylim(0,1)
# plt.xlim(0,20)
# plt.legend()
# plt.show()

# Zad3

# x3 = np.arange(0,30,0.1)
# z = np.sin(x3)
# t = np.cos(x3)
# plt.plot(x3,z,label="sin")
# plt.plot(x3,t,label="cos")
# plt.legend()
# plt.show()

# Zad4
# y3 = np.sin(x3)
# z2 = np.sin(x3+np.pi)
# plt.title("wykres sin")
# plt.ylabel("sin")
# plt.xlabel("x")
# plt.plot(x3,z2)
# plt.plot(x3,y3+2)
# plt.show()

 # Zad5


# Zad6


# Zad7
# csv = pd.read_csv('zamowienia.csv',sep=';')
# sumy = csv.groupby(['Sprzedawca']).agg({'Utarg':['sum']})
# suma_og = sum(csv['Utarg'])
# sumy = (sumy/suma_og)*100
# sumy = round(sumy)
# plt.show()