# Crie um programa que tenha uma dupla totalmente preenchida 
# com uma contagem por extenso, de zero até vinte. Seu programa 
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

numero = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezeseis','dezesste','dezoito','dezenove','vinte')

n=int(input('Digite um numero entre 0 e 20: '))
while 0 < n > 20 :
      n=int(input('inválido. Digite um numero entre 0 e 20: '))

print(f'O {n} por extenso é {numero[n]}')
