#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area
#e a quantidade de tinta para pintala ,sabendoo que cada litro de tinta pinta uma area de 2m²
Largura = float(input('informe a largura da parede que deseja pintar: '))
altura = float(input('Infomre a altura da parede que deseja pintar: '))
area = Largura * altura
tinta = area / 2
print('A area da parede é de {}m²'.format(area))
print('Para pintar essa parede você precisará de {} Litros de tinta'.format(tinta))

