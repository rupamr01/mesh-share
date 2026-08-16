import socket
s1= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(("localhost",6982))
s1.send("hello my name is this i hope this is woking".encode())
s1.send("data bhej diya".encode())
s1.close()