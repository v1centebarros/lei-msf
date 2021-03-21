#Biblioteca criada para fazer a Regressão Linear
from LinearRegression import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#Definição das amostras
l = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0])
x = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])

#Alínea a) / b) / c)
#Usando a Biblioteca de Regressão linear calcular...
li = LinearRegression(l,x)
print(li)
#Plot dos pontos x, f(x), MODO = 'ro'=> Apenas os pontos
plt.plot(l,x,'ro')

#Alínea d)
#Criação de um array com 10000 valores entre o mínimo e o máximo de x (neste caso é o l)
#IMPORTANTE: multiplica-se por 0.9 e por 1.1 para que caso haja um valor no mínimo e no máximo da amostra, ele possam ser vistos
x1 = np.linspace(np.min(l)*0.9, np.max(l)*1.1, 10000)

#Plot da funcão (x,f(x))
plt.plot(x1,x1*li.m()+li.b())

#Alínea e)
#Calcular e mostrar o f(165.0), neste caso x(165.0)
print (f"x(165.0) = {li.m()*165.0+li.b()}")

#Plot ponto x(165.0) com uma cor diferente
#IMPORTANTE: Como é só um ponto é preciso colocar o formato 'ro'
plt.plot(165.0, li.m()*165.0+li.b(),'ro',color='green')

#Alínea f)
#Não percebi o que era para ser feito

plt.show()