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
            self.con.send(self.aluno)


# função esperar - Thread
def esperar(socket_tcp, send, host='', port=5000):
    origem = (host, port)
    # cria um vinculo
    socket_tcp.bind(origem)
    # deixa em espera
    socket_tcp.listen(1)

    while True:
        # aceita um conexão
        con, cliente = socket_tcp.accept()
        print('Cliente ', cliente, ' conectado!')
        # atribui a conexão ao manipulador
        saida.con = con

        while True:
            # aceita uma mensagem
            aluno = con.recv(1024)
            if not aluno: exit()
            print(str(aluno.nome, 'utf-8'))


if __name__ == '__main__':
    # cria um socket
    socket_tcp = socket(AF_INET, SOCK_STREAM)
    saida = Send()
    # cria um Thread e usa a função esperar com dois argumentos
    thread = Thread(target=esperar, args=(socket_tcp, saida))
    thread.start()

    print('Iniciando o servidor de chat!')
    print('Aguarde alguém conectar!')

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
