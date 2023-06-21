print('--- Sequência de fibonacci ---')

t1 = 0
t2 = 1

n = int(input('Quantos termos você quer mostrar: '))
print('{} -> {}'.format(t1, t2), end='')

cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' -> {}'.format(t3), end='')
    cont += 1
print(' -> fim')
