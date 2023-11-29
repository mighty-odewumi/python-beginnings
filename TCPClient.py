import socket

tgtHost = '127.0.0.1'
tgtPort = 63342


#This code below is a TCP client
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((tgtHost, tgtPort))
conn.send(b'Whois')
banner = conn.recv(4096)
print(banner)


'''
#The code below is a UDP client
con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
con.sendto(b'hello',(tgtHost, tgtPort))
data, addr = con.recvfrom(4096)
print(data)
'''
