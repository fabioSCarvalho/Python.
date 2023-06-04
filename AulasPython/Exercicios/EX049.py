#Refaça o DESAFIO 009, mostrando a tabuada de um número que
# o usuário escolher, só que agora utilizando um laço fo
tab = int(input("Digite um numero para ver a tabuada: "))
for n in range(0, 11):
    print("{} X {:2} = {:2}".format(tab, n, tab * n))
