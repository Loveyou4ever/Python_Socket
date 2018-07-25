import socket
import os


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('172.25.99.110',9090))
print('Client start!')
sock.send(bytes('客户端:)\n',encoding='utf-8'))   # str 类型 -> bytes 类型，发送，\n必须要，前面的 server 是按行读取的
print(str(sock.recv(1024),encoding = 'utf-8'))    # bytes 类型 -> str 类型，接受
#os.system(str(sock.recv(1024)))

sock.close()
print('Client end!')
