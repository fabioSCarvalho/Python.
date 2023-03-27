# Faça um programa que leia um ângulo qualquer e mostre a  
# tela o Valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians
angulo = float(input('informe o ângulo que você deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
print('o angulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))



