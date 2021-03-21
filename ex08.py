import numpy as np
import matplotlib.pyplot as plt

#Definição das amostras
t = np.linspace(200, 1100, 10)
e = [0.6950, 4.363, 15.53,38.74,75.08,125.2, 257.9, 344.1, 557.4,690.7]

#Alínea a)
#Não é Linear
plt.plot(t,e,'ro')

#Alínea b)
tlog = np.log(t)
elog = np.log(e)

#Calcular o declive e a ordenada na origem com os valores de log
c1 = np.polyfit(tlog,elog,1)

#Gerar array com 100 valores 
x = np.linspace(min(tlog) -0.1, max(elog) + 0.1, 100)

plt.plot(x,x*c1[0]+c1[1],color="blue")

#TODO terminar exercício na aula

plt.show()