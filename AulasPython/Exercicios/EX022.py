#Crie um programa qie çeoa o nome completo de uma pessoa e mostre
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras tem ao todo(sem considerar os espaços)
# - Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip

nome2 = nome.split()


print('Nomde maiusculo:{}'.format(nome.upper()))
print('Nomde maiusculo:{}'.format(nome.lower()))
print('SEu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} Letras'.format(nome2[0], len(nome2[0])))


