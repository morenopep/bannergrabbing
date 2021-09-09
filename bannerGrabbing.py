#!/usr/bin/python

import socket,sys

ip = raw_input("Digite o IP: ")
porta = input("Digite a Porta: ")

    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.connect((ip,porta))
    banner = meusocket.recv(1024)
    print banner