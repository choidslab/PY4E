import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # tuple 형태로 connect 정보 전달
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) # 서버로 요청 전송

while True:
    data = mysock.recv(512) # 512 bytes 수신
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
