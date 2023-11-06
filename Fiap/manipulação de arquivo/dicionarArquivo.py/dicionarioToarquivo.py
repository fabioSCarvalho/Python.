usuarios={}
email = []

opc = "S"



while True:

    print('''

    [1] Cadastrar usuario

    [2] Listar usuarios

    [3] Deletar usuarios

    [4] Pesquisar usuarios

    [5] Salvar

    [6] Exit

    ''')

    resp = int(input("Opcção desejada: "))


    if resp == 1:

        while opc == "S":   

            email.append(input("email: ").strip())

            opc = input("Deseja continuar: [S] [N]").upper()
        for email in email:
            print(email)
            usuarios[(email)]=[input("Nome: "), input("Setor: "), input("Cracha: ")]
    

    if resp == 2:

        for usuario, dados in usuarios.items():

            print("-=-" * 10)

            print(f'email: {usuario}')

            print(f'Nome: {dados[0]}')

            print(f'Setor: {dados[1]}')

            print(f'Cracha: {dados[2]}')

            print("-=-" * 10)
            

    if resp == 3:

        deletar = input("Informe o emai do usuaio: ").strip() 
        if  usuarios.get(deletar)  != None: 
            del usuarios[deletar]

        print("Deletado")


    if resp == 4:
        lista = usuarios.get(input("Informe o emai do usuaio: ").strip())

        if lista != None:

            print(f"Nome: {lista[0]}")

            print(f"Setor: {lista[1]}")

            print(f"Cracha: {lista[2]}")


    if resp == 5:

        with open("usuarios.txt", "a") as arquivo:
            for usuario, dados in usuarios.items():
               arquivo.write(f"{usuarios} ; {dados}  \n") 

    if resp == 6:

        break;