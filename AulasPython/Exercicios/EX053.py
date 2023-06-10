# Crie um programa que leia uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper().split()
palavraJunta = ''.join(frase)
inverso = palavraJunta[::-1]

'''
cont = len(palavraJunta) - 1

for letra in range(cont,-1, -1):
    inverso += palavrajunta[letra]
'''

print(inverso)
print(palavraJunta)

if inverso == palavraJunta:
    print('TEmos um palindromo')
else:
    print("A frase não é um palindromo")

