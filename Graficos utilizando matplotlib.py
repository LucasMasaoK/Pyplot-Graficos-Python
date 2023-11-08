import matplotlib.pyplot as plt
import random

anos=[1950,1960,1970,1980,1990]

arrecadacao=[random.randrange(1,10000),random.randrange(1,10000),random.randrange(1,10000),random.randrange(1,10000),random.randrange(1,10000)]
custo=[random.randrange(1,10000),random.randrange(1,10000),random.randrange(1,10000),random.randrange(1,10000),random.randrange(1,10000)]

plt.plot(anos,arrecadacao, color="green", marker=10, linestyle='dotted')
plt.plot(anos,custo, color="red", marker=10, linestyle='dotted')

plt.title("Produto nominal")

plt.ylabel("Bilhoes de R$")

plt.show()