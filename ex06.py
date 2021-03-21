from LinearRegression import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#Definição das amostras
#Aqui foi usada a função `linspace` para gerar o array de tempo automaticamente
t = np.linspace(0, 9, 10)
d = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.355, 5.666, 5.329])

#Alínea a)
plt.plot(t,d,'ro')

#Alínea b)
li = LinearRegression(t,d)
print(li)

#Alínea c)
#É igual ao declive
print(f"Vm = {li.m()}")

#Alínea d)
c1 = np.polyfit(t,d,1)
print(c1)
# Dá para ver que os valores obtido em b) são semelhantes aos obtidos com a função polyfit

#Alínea e)
v = c1[0] * 60
print(f"v={v}km/h")

#NOTA: Não pede para dar plot da reta, mas vou fazer à mesma
plt.plot(t,t*li.m()+li.b())

plt.show()