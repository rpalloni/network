# run the network_socket_server and than the network_socket_client
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
IPv4 = socket.AF_INET # Internet address family
TCP = socket.SOCK_STREAM # Socket type (protocol used to transport the message)

# context manager: no need to call s.close()
with socket.socket(IPv4, TCP) as s:
    s.bind((HOST, PORT)) # associate the socket with a specific network interface and port number > values depends on address family
    s.listen() # listening socket object: accepts new connections from clients
    conn, addr = s.accept() # communication socket object: exchanges data with connected clients
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data) # srves only ONE client and then exits

# netstat --listening --tcp
# Active Internet connections (only servers)
# Proto Recv-Q Send-Q Local Address           Foreign Address         State
# tcp        0      0 localhost:65432         0.0.0.0:*               LISTEN
