from socket import * 
servidor =  "Localhost"
porta = 43210

msg = bytes(input('Digite algo: '), 'utf-8') #Recebe a mensagem e converte para bytes e defini padrão utf8

obj_socket = socket(AF_INET, SOCK_STREAM) #Se indeificar com o ip e defini o protocolo tcp (O mesmo do servidor) 
obj_socket.connect((servidor,porta)) # conecta com ultilizando o servidor e a porta definidos no inicio
obj_socket.send(msg) #envia a mensagem
resposta = obj_socket.recv(1024) # Recebe um resposta com até 1024 bytes

print("REcebemos :", resposta)
obj_socket.close()
