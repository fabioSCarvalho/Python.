#Ecreva um programa que leia a bvelocidade de um carro.
#Se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,,00 por cada km acima do limite.

velocidade = str(input('Infome a velocidade do carro: Km/h: ')).strip()
km = float(velocidade)
if km > 80 :
    multa = (km - 80) * 7.00
    print('Velocidade acima do permitido!! Você foi multado')
    print('Valor da multa: R${:.2f}'.format(multa))
else:
    print('Velocidade permitida, boa viagem')

