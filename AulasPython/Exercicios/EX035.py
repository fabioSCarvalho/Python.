
# faça um programa que diga se os segmentos podem formar um triangulo
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceito segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmento a cima não podem formar um triangulo')