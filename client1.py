import socket

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = raw_input("Enter server IP: ")
port = 1337

S.connect((host, port))

S.send(raw_input("Enter command: "))

print S.recv(1024)

S.close()


# Tyler's Server: 138.247.97.232
# Anthony's Server: 138.247.96.218
# Andy's Server: 138.247.96.222
# Peter's Server: 138.247.96.57
# Logan's Server: 138.247.96.246
# Michael's Server: 138.247.96.240
# Steven's Server: 138.247.96.1
# Levi's Server: 138.247.97.59