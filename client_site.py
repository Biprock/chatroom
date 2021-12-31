import socket
import sys
import select

server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if len(sys.argv) != 3:
     print("Correct Usage: script , IP Adress , Port number")
     exit()
     
IP_Adress = str(sys.argv[1])

port = int(sys.argv[2])

sockets_list = [sys.stdin, server]

read_sockets, write_sockets,error_sockets=select.select(sockets_list,[],[])

for socks in read_sockets:
    if socks==server:
        message = socks.recv(2048)
        print(message)
    else:
        message=sys.stdin.readline()
        server.send(message)
        sys.stdout.write("<YOU>")
        sys.stdout.write(message)
        sys.stdout.flush()

server.close()