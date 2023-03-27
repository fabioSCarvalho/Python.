#Faça um programa que leia a nota de um aluno calcule e mostrea sua média
media = float
nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('A media entre {:.1f} e {:.1f} é {:.1f} '.format(nota1, nota2, media))
