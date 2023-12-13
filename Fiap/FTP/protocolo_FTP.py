from ftplib import *
ftp_ativo = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
usuario = input("digite o usuario: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)
print("diretorio atual de trabalho: ", ftp.pwd())
ftp.cwd('pub')
print("diretório atual de tabalho: ", ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit()
