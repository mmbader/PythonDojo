import socket

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect(("www.pythonlearn.com", 80))
socket_obj.send("GET /code/intro-short.txt HTTP/1.0\nHost: www.pythonlearn.com\n\n")
content = ""

while True:
    data = socket_obj.recv(512)
    content += data

    if len(data) < 1:
        break
socket_obj.close()

pos = content.find("\r\n\r\n")
print content[pos+4:]

