from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from aluno import Aluno


# classe para manipular o socket
class Send:
    def __init__(self):
        self.aluno = None
        self.con = None

    def escrever(self, aluno):
        self.aluno = aluno
        if self.con != None:
            # envia um mensagem atravez de uma conexão socket
            self.con.send(object(self.aluno))


# função esperar - Thread
def esperar(socket_tcp, saida, host='localhost', port=5000):
    destino = (host, port)
    # conecta a um servidor
    socket_tcp.connect(destino)

    if not socket_tcp:
        print('Erro de conexao')

    while True:
        print('Conectado a ', host, '.')
        # atribui a conexão ao manipulador
        saida.con = socket_tcp
        while True:
            # aceita uma mensagem
            aluno = socket_tcp.recv(1024)
            if not aluno: exit()
            print(str(aluno.nome, 'utf-8'))


if __name__ == '__main__':
    print('Digite o nome ou IP do servidor(localhost): ')
    host = input()

    if host == '':
        host = '127.0.0.1'

    # cria um socket
    socket_tcp = socket(AF_INET, SOCK_STREAM) 
    saida = Send()
    # cria um Thread e usa a função esperar com dois argumentos
    thread = Thread(target=esperar, args=(socket_tcp, saida, host))
    thread.start()
    print('')

    aluno = Aluno()

    aluno.nome = input()
    aluno.matricula = int(input())
    while True:
        saida.escrever(aluno)
        aluno.nome = input()
        aluno.matricula = int(input())

    thread.join()
    socket_tcp.close()
    exit()
