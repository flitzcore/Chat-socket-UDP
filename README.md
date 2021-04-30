# Chat-socket-UDP
Untuk program ini, dibutuhkan 2 file:
## Client
Pertama melakukan persiapan dan menyiapkan koneksi
```
import socket
import threading


clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
```
Disini digunakan SOCK_DGRAM untuk menandakan metode koneksi UDP. Setelah itu memasukkan alamat server
```
udp_host = socket.gethostname()		
udp_port = 6789	
```
Setelah memasukkan alamat server, dibuat fungsi untuk mengirim dan menerima informasi
```
def Kirim():
    while True:
        msg=input("")
        clientSock.sendto(msg.encode('utf-8'),(udp_host,udp_port))
def Terima():
    while True:
        data,_=clientSock.recvfrom(1024)
        dataTerima=data.decode('utf-8')
        print(dataTerima)
 ```
Kedua fungsi ini harus dapat berjalan di waktu yang sama, oleh karena itu memerlukan metode threading dengan cara:
 ```
k=threading.Thread(target=Kirim)
t=threading.Thread(target=Terima)  
```
Setelah itu,dibutuhkan satu lagi fungsi untuk mendaftarkan nama di server, berupa:
```
def daftar():
    nama=bytes(input('Enter name:'),'utf-8')
    clientSock.sendto(nama,(udp_host,udp_port))#daftar  
```
Setelah fungsi ini dipanggil, client akan menunggu balasan server. Jika  nama yang diajukan sudah ada, client diminta menuliskan nama baru
```
while True:
    konfirmasi,_=clientSock.recvfrom(1024)
    konfirmasi=konfirmasi.decode('utf-8')
    if konfirmasi=='nama ini sudah diambil':
        print(konfirmasi)
        daftar()
    else:
        k.start()
        t.start()
        break
```
Disini sudah beres mengenai client

## Server
Pertama melakukan persiapan dan menyiapkan koneksi
```
import socket

UDP_IP_ADDRESS = socket.gethostname()
UDP_PORT_NO = 6789

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
```
Hal ini dilakukan dengan cara yang hampir mirip dengan client. Disini menggunakan metode bind untuk menghubungkan server. 
```
Alamat=[]
Nama=[]
```
Setelah itu, dibuat 2 list untuk menyimpan nama serta alamat client
```
def broadcast(message):
    for a in Alamat:
            serverSock.sendto(message,a)
```
Disini disediakan fungsi broadcast untuk mengirimkan pesan pada seluruh client
```
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
            if msg in Nama:
                serverSock.sendto('nama ini sudah diambil'.encode('utf-8'),addr)
            else:
                Alamat.append(addr)
                Nama.append(msg)
                welcomeMSG=f'{msg} has joined the chat'.encode('utf-8')
                broadcast(welcomeMSG)

Terima()
```
Selain itu disediakan fungsi terima untuk menerima data dari client. Jika alamat client tidak pernah ditambahkan ke list Alamat, maka nama client akan dilihat dan dicocokkan dulu di daftar nama. Jika nama sudah diambil, client diminta mengirimkan nama. Jika nama belum diambil, alamat dan nama client akan disimpan. Setelah itu dikirimkan pesan ke semua client bahwa ada client yang masuk. Jika alamat client sudah ada di list Alamat, pesan client akan disampaikan pada semua client.
