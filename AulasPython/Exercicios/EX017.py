#Faça um programa que leia o comprimento do cateto oposto e do cateto 
#adjacente de um triânculo retângulo, calcule e mostre o comprimento da hipotenusa
import math
co = float(input('Comprimetno do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = math.hypot(co,ca)

#hi = ((co ** 2 )+ (ca ** 2)) ** (1/2)

print('A impotenusa vai medir {:.2f}'.format(hi))
