''' Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos. '''

pesoMaior = 0
pesoMenor = 0
for kg in range(1, 6):
    peso = float(input('Informe o {}° peso: '.format(kg)))
    if kg == 1:
        pesoMenor = peso
        pesoMaior = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        elif peso < pesoMenor:
            pesoMenor = peso
print('o maior peso foi {} Kg'.format(pesoMaior))
print('o menor peso foi {} Kg'.format(pesoMenor))
