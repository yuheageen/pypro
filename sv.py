import socket

s = socket.socket(socket.AF_SOCK,0)
s.bind("",)
s.listen()
reply,sabdr = s.recyfrom(1000)

print(ip,astr)