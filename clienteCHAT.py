#!/usr/bin/python
# -*-coding:utf-8-*-

import socket
from threading import Thread
'''Teste'''
class VerificaMensagens(Thread):
    def __init__(self, tcp):
        Thread.__init__(self)
        self.tcp_cliente_socket = tcp

    def run(self):
        self.tcp_cliente_socket = tcp
        self.fechar = False
        while (not self.fechar):
            # Aqui, o servidor aguarda a chamada do cliente para enviar a msg para outros clientes
            data = self.tcp_cliente_socket.recv(1024)
            if (data):
                msg = str(data)  # transforma a msg recebida em str
                print(msg[2:-1]) # mostra somente do terceiro caractere até o penultimo(oculta o 'b ')
        print('saiu do laco')

    def fecharVerificaMensagens(self):
        self.fechar = True
        self.tcp_cliente_socket.close()


# MAIN

# setar aqui o endereço IP do servidor
# HOST = "192.168.1.21"
HOST = ''
PORT = 5100

HOST = str(input('Digite o IP do servidor: ')).strip()

# cria uam variável e atribui um objeto tipo socket
# socket.AF_INET = O endereço é composto pelo IP e PORTA
# spcket.SOCK_STREAM = utiliza o protocolo TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta com o servidor, passando o IP e a PORTA como parâmetros
tcp.connect((HOST, PORT))

# Recebe o Nome do usuário
nome = str(input('Digite seu nome: '))

# Chama a classe para verificar as msg que sao enviadas pelos clientes ao servidor
# .start - Inicia a Verificação, e recebe caso alguma msg tenha sido enviada ao servidor
verificaMsg = VerificaMensagens(tcp)
verificaMsg.start()

print('Bem-vindo(a), {}!'.format(nome.title()))
print('Seu ip é {}'.format(tcp.getsockname()[0]))
print(23 * '-')
texto = ''

# Inicia o loop para enviar as msg ao servidor e o servidor envia aos outros clientes
# Se for digitado a palavra sair, o loop é encerrado, fechando a conexão com o servidor.
while texto.lower() != 'sair':
    texto = str(input())
    tcp.send(bytes(nome.title() + ' diz: ' + texto, 'utf-8'))

# Sai da classe que verifica as msg recebidas
verificaMsg.fecharVerificaMensagens()
print('finalizado')
