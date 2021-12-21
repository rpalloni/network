# run the network_socket_server and than the network_socket_client
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
IPv4 = socket.AF_INET # Internet address family
TCP = socket.SOCK_STREAM # Socket type (protocol used to transport the message)

# context manager: no need to call s.close()
with socket.socket(IPv4, TCP) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
