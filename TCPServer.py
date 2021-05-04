import os
import sys
from socket import *
import http.server

host = ''
port = 11297
BUFFER_SIZE = 65535

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('연결 성공')
    try:
        message = connectionSocket.recv(BUFFER_SIZE).decode()  # 소켓으로부터 데이터를 수신
        filename = message.split()[1]
        #print('파일명: ' + filename[1:])

        # f = open(filename[1:], 'r', encoding='UTF8')
        f = open("file", 'r', encoding='UTF8')
        output_data = f.read()

        # Send one HTTP header line into socket
        header = 'HTTP/1.0 200 OK\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.send('\r\n'.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(output_data)):
            connectionSocket.send(output_data[i].encode())
        connectionSocket.send('\r\n'.encode())

    except IOError:
        # Send response message for file not found
        print('IO Error')
        header = 'HTTP/1.0 404 Not Found\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.send('\r\n'.encode())

    connectionSocket.close()

    print("연결을 종료합니다.")
    serverSocket.close()

    os.system("pause")
    sys.exit()  # Terminate the program after sending the corresponding data

