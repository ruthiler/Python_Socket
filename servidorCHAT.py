import socket
from threading import Thread

HOST = ''
PORT = 5100

# Pega o numero de IP na rede do Servidor
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# Verifica as msg recebidas pelos clientes e direciona para todos os clientes conectados
class verificaMensagensClientes(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn
        print('criada a thread')
    def run(self):
        print('RODANDO A THREAD')
        global listaConectados
        for i in listaConectados:
            print(listaConectados)
        while (1):
            data = self.conn.recv(1024)
            msg = str(data)
            print('>> ' + msg[2:-1])
            for conexao in listaConectados:
                if(conexao != self.conn):
                    conexao.send(data)
        
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_server_socket.bind((HOST, PORT))
tcp_server_socket.listen(2)

print('Nome do servidor: ' + socket.gethostname())
print('IP do Servidor: ' + get_ip_address())
print('Porta: {}'.format(PORT))



conectados = 0
listaConectados = []
listaThread = []

# Aguarda que pelo menos 2 clientes estejam conectados para iniciar o bate-papo
# Quando dois ou mais clientes conectarem inicia o loop
while (conectados<2):
    print('Conectados: {}'.format(str(conectados)))
    conn, addr = tcp_server_socket.accept()
    temp = verificaMensagensClientes(conn)
    listaThread.append(temp)
    listaConectados.append(conn)
    conectados+=1

for i in listaConectados:
    print('conetado por'.format(i))


print('comecou')
print(len(listaThread))
for i in listaThread:
    i.start()
    print('ativando as threads')

# Continua aceitando mais clientes
while 1:
    print('Conectados: '.format(str(conectados)))
    conn, addr = tcp_server_socket.accept()
    temp = verificaMensagensClientes(conn)
    listaThread.append(temp)
    listaConectados.append(conn)
    temp.start()
    conectados+=1

for i in listaConectados:
    i.close()

