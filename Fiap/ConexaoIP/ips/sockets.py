import socket
resp ='S'
while resp =='S':
    url=input('Digite uma url: ')
    ip=socket.gethostbyname(url)
    print('O ip referente é a URL informada: ', ip)
    resp=input('Digite <S> para continuar: ').upper()

