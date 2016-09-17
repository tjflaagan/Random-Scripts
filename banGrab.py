#!/usr/bin/python  
import socket  
import sys  
import os  
#grab the banner  
def grab_banner(ip_address,port):  
    try:  
         s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
         s.connect((ip_address,port))
         s.send("abcdef")
         banner = s.recv(1024)  
         print ip_address + ':' + banner  
    except:  
         return  

def main():  
    portList = [21,22,23,25,5900,6667]   
    for port in portList:  
        ip_address = '192.168.65.137' 
        grab_banner(ip_address,port)  
if __name__ == '__main__':  
    main()  