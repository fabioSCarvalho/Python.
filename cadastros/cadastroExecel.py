usuarios = {}
emaill= []
resp = "S"

while resp != "N":
    emaill.append(input("Informe o e-mail: ").strip())
    resp = input("Deseja continuar: [S] [N] ").strip().upper()

cadastro = list(enumerate(emaill))

for usuario in range(0, len(cadastro)):
    print("Usuario: ", cadastro[usuario][1])
    usuarios[cadastro[usuario]]=[input("Nome completo: "), input("Setor: "), input("Cracha: ")]

with open("usuario.csv", "w") as arquivo:
    arquivo.write("Ususario; Email; Nome; Setor; Cracha \n")


with open("usuario.csv", "a") as arquivo:
    for usuario, dado in usuarios.items():
        arquivo.write(f"{usuario[0]}; {usuario[1]}; {dado[0]};{dado[1]};{dado[2]} \n")