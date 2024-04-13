from socket import *
localhost="Localhost"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM) #Tipo de identificação o IP, trabalho com tcp
obj_socket.bind((localhost,porta)) #endereço para procurar, porta de entrada
obj_socket.listen(2) #maximo de cliente para acessar a aplicação
print("Aguardando cliente...")
while True:
    con, cliente = obj_socket.accept() #espera um cliente até se conectar
    print("Conectando com: ", cliente) # quando conectado retorna o Ip do cliente
    while True:
        msg_recebida = str(con.recv(1024)) # informa o tamanho maximo do pacote que pode receber em bytes
        print("Recebemos: ", msg_recebida)
        msg_enviada = bytes(input(" Responda: "), 'utf-')
        con.send(msg_enviada)
        break
    con.close 
