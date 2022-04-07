import  socket
host = "203.250.133.88"
port = 11954
Buffer_SIZE = 128

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_address = (host,port)
sock.bind(server_address)
client_socket, address = server_address.accept

while True:
    print("waiting for requsts")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from %s prot %s"%client_address)
    sock.sendto(message,client_address)
sock.close()
