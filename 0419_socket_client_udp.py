import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['erick', 'zhao', 'xinjiang']:
    s.sendto(data, ('127.0.0.1', 9999))
    print s.recv(1024)
s.close()