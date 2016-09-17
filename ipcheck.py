
#run with python3
import ipaddress

def ipinrange(ip):
	add1 = ipaddress.ip_network(ip)
	for hosts in add1:
		print(hosts)
def octetbin(length, ip):
	num = (bin(int(ipaddress.IPv4Address(ip))))
	num = num.split('b',2)[1]
	l = [''.join(x) for x in zip(*[list(num[z::length]) for z in range(length)])]
	print(l)
def definenet(ip):
	add2 = (ipaddress.ip_network(ip))
	x = 0
	print ('Network: ' + str(add2.network_address))
	print ('Gateway: ' + str(add2.network_address + 1))
	print ('Broadcast: ' + str(add2.broadcast_address))
	print ('Wildcard: ' + str(add2.hostmask))
	if(add2.is_private):
		print('Private Address')
	if(add2.is_multicast):
		print('Multicast Address')
	if(add2.is_reserved):
		print('Reserved Address')
	for i in add2:
		x = x + 1
	print ('Block Size: ' + str(x))
	print ('Usable: ' + str(x-2))



ipinrange('192.168.1.0/24')
octetbin(8, '192.168.1.1')
inputaddr = input("Input IPv4 address: ")
definenet(inputaddr)
print('Success')


