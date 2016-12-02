import socket

ip = "127.0.0.1"
ports = [20, 21, 23, 25, 80, 443, 530, 8080]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3) #3 seconds timeout

for port in ports:
    if s.connect_ex((ip, port)) == 0:
        print("Port ",port," is open")
    else:
        print("Port ",port," is closed")
