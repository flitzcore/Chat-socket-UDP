
import socket
import threading

nama=bytes(input('Enter name:'),'utf-8')

clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

udp_host = socket.gethostname()		
udp_port = 6789			        


clientSock.sendto(nama,(udp_host,udp_port))#daftar

def Kirim():
    while True:
        msg=input("")
        clientSock.sendto(msg.encode('utf-8'),(udp_host,udp_port))
def Terima():
    while True:
        data,_=clientSock.recvfrom(1024)
        print(data.decode('utf-8'))

k=threading.Thread(target=Kirim)
t=threading.Thread(target=Terima)  
k.start()
t.start()

