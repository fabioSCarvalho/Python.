# Faça um programa que faça uma Contagem regressiva
# Com estouro de fogos do 10 ao 0 com pausa de 1 segundo
import time
print("-=" * 10)
print("Contagem regressiva")
print("-=" * 10)

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print(" caboommmm")
