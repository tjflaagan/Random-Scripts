import socket
import argparse
import sys
import select
from thread import *


def prompt():
    sys.stdout.write('<You>')
    sys.stdout.flush()


def handle_client(socket):

    done = False

    while 1:
        sockets = [socket]
        read_socks, write_socks, error_socks = select.select(sockets, [], [])
        for sock in read_socks:
            if sock == socket:
                data = sock.recv(4096)
                if not data:
                    print '\n[*] Disconnected from server'
                    done = True
                    break
                else:
                    sys.stdout.write(data)
                    prompt()
        if done:
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Chat Client',
                                     description='Chat with server')
    parser.add_argument('host',
                        type=str,
                        help='IP of remote host')
    parser.add_argument('port',
                        type=int,
                        help='Port of remote host')

    args = parser.parse_args()
    host = args.host
    port = args.port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((host, port))
    except socket.error, err:
        print '[!]', err
        sys.exit()

    print '[*] You are connected!'
    prompt()

    start_new_thread(handle_client, (s,))

    while 1:
        msg = sys.stdin.readline()
        try:
            s.send(msg)
        except:
            sys.exit()
        prompt()

