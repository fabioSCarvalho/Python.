# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input("Primeiro termo da PA: "))
razao = int(input('Razão da PA'))
decimo = primeiro + (11 - 1) * razao
for n in range(primeiro, decimo, razao):
    print(n, end=" -> ")
print("Finish")
