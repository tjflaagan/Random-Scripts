import socket

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())

port = 1337

S.bind((host, port))

S.listen(5)

while True:
    c, addr = S.accept()
    print "Connection from: ", addr
    data = c.recv(1024)
    if ("ECHO" in data):
        print addr, data
        c.send(data[5:])
    elif ("TIME" in data):
        print addr, data
        c.send("Thur")
    elif ("MOTD" in data):
        print addr, data
        c.send("Welcome to GenCyber")
    elif ("YELLBACK" in data):
        print addr, data
        c.send(data[9:].upper())
    else:
        c.send("INVALID ENTRY\nAvailable Commands:\n \
            ECHO <Data>\nTIME\nMOTD\nYELLBACK")

    c.close()