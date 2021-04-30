
import socket
import threading

UDP_IP_ADDRESS = socket.gethostname()
UDP_PORT_NO = 6789

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

Alamat=[]
Nama=[]


def broadcast(message):
    for a in Alamat:
            serverSock.sendto(message,a)
def Terima():
    while True:
        print("waiting for client")
        msg, addr = serverSock.recvfrom(1024)
        msg=msg.decode('utf-8')
        if addr in Alamat:
            index=Alamat.index(addr)
            editedMSG=f'{Nama[index]}: {msg}'
            broadcast(editedMSG.encode('utf-8'))
        else:
            Alamat.append(addr)
            Nama.append(msg)
            welcomeMSG=f'{msg} has joined the chat'.encode('utf-8')
            broadcast(welcomeMSG)

t=threading.Thread(target=Terima)
t.start()



    
    
    
    

