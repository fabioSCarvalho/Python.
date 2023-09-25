from time import sleep

cadastro={}

#função cadasrar novo usuario
def casdastrar(dicionario):
    resp = 'S'
    listEmail=[]

    #Recebendo email enquanto resposta for sim "S"
    while resp =='S':
        email = input('Digite o email: ') #Validando o email quando ele tiver "@"
        if '@' in email:
            listEmail.append(email)
            resp = input('Deseja continuar: ').upper()
        else:
            resp = input('Email inválido. Deseja tentar novamente: [S] [N]').upper()

    listEmail = list(enumerate(listEmail))     #criando uma lista de email com seus respecitivos numero
    for email in range(0, len(listEmail)):
        print('E-mail: ', listEmail[email][1])
        dicionario[listEmail[email]]=[input('nome completo: '), input('setor: '),input('cracha: ')]


#Função para lista os usuario cadastrados
def listarUsuario(dicionario):
    for chave,dado in dicionario.items():
        print('-=-='*10)
        print('Usuario: ', chave[0] + 1)
        print('e-mail: ', chave[1])
        print('nome: ', dado[0])
        print('setor: ', dado[1])
        print('cracha: ', dado[2])
        print('-=-='*10)


#exportar para exel
def excel(dicionario):
    nomeArquivo = input('Nome do aquivo: ')
    with open(f'{nomeArquivo}.csv', 'a') as arquivo:
        arquivo.write("Usuario ; e-mail ; Nome ; Setor ; cracha \n")
        for chave, dado in dicionario.items():
            arquivo.write(f"{chave[0]}; {chave[1]} ;  {dado[0] } ;  {dado[1] } ; {dado[2]} \n")
    print('ok')


#Menu
def menu():
    print('''
            [1] Cadastrar
            [2] Listar Usuarios 
            [3] Exportar parar CSV (Excel)
            [5] Ler arquivo Excel 
            [5] Sair
                ''')
    opc = input('Digite a opção desejada: ').strip

def importar(arquivo):
    with open("cadastro.csv", "r") as excel:
        arquivo = excel.readlines()
        for linha in arquivo:
            dado = linha.split(";")
            print('Usuario: ', dado[0])
            print('E-mail: ', dado[1])
            print('Nome: ', dado[2])
            print('Setor: ', dado[3])
            print('Cracha: ', dado[4])
            

while True:
    print('''
            [1] Cadastrar
            [2] Listar Usuarios 
            [3] Exportar parar CSV (Excel)
            [5] Ler arquivo Excel 
            [5] Sair
                ''')
    
    opc = input('Digite a opção desejada: ').strip()

    if opc == '1':
        casdastrar(cadastro)
    elif opc == '2':
        listarUsuario(cadastro)
    elif opc == '2':
        excel(cadastro)
    elif opc == '3':
        excel(cadastro)
    elif opc == '4':
        importar(cadastro)
    elif opc == '5':
        print('saindo ... ')
        sleep(5)
        print('encerrado')
        break
    else:
        print('Opção incorreta. Tente novamente!! ')
        menu()

