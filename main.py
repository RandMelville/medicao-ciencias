import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

days = np.arange(7)

temperatures = [random.randrange(20,35)]

for x in range(len(days)-1):
    temperatures.append(temperatures[x] + random.randrange(-4,4))

temperatures = np.array(temperatures)

print(days)
print(temperatures)

slope, intercept, _,_, std_err = linregress(days, temperatures)
line = slope*days+intercept

plt.plot(days, temperatures, label='Temperaturas')
plt.plot(days, line,label='Regressão linear das temperaturas', color='red')
plt.axhline(np.mean(temperatures), label='Temperatura média', color='orange', linestyle='dashed')
plt.axhline(np.median(temperatures), label='Mediana das temperaturas', color='green', linestyle='dashed')

plt.title("Temperaturas registradas durante uma semana")
plt.ylabel("Temperatura em °C")
plt.xticks(days,["domingo","segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"])
plt.legend()
plt.show()
