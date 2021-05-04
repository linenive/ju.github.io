import os
import sys
from socket import *

ip = 'localhost'
port = 11297
BUFFER_SIZE = 65535

print("파일 이름을 입력하세요(file): ", end=' ')
file_name = input()

clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((ip, port))
except ConnectionRefusedError:
    print("연결 실패")
    clientSocket.close()
    sys.exit()

print("연결 되었습니다.")

# Send one HTTP header line into socket
# Fill in end
header = 'GET /' + file_name + ' HTTP/1.0\r\n\r\n'
clientSocket.send(header.encode())
print("메시지를 전송했습니다.")

data = ''
while True:
    clientSocket.settimeout(5)
    new_data = clientSocket.recv(BUFFER_SIZE).decode("utf-8")
    if len(new_data) == 0:
        break
    data += new_data
print(data)
print("연결을 종료합니다.")
clientSocket.close()

os.system("pause")
