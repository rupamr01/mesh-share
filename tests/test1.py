import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket bana diya!")
print(s)
s.bind(("localhost",6982))

s.listen(1)
conn, addr = s.accept()
data=conn.recv(1024)
print("data aagya ")
print(data)
print(data.decode())
conn.close()
s.close()