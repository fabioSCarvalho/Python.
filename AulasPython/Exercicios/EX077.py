#Crie uma tupla com varias palavras. Depois disso, você deve mostrar para cada palavra , quais são  suas vogais
palavra = ('aprender','programar','linguagem','python','curso')

for item in palavra:
    print(f'\n Na palarvra "{item.upper()}" temos', end=' ')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(f' {letra}' , end=' ')