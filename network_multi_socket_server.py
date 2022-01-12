# handle multiple client connections
# run the network_multi_socket_server and than many network_socket_client
import socket
import asyncio

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 6550         # Port to listen on (non-privileged ports are > 1023)
IPv4 = socket.AF_INET # Internet address family
TCP = socket.SOCK_STREAM # Socket type (protocol used to transport the message)


async def handle_client(conn, addr, loop):
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(conn, 255)).decode('utf8') # str
        await loop.sock_sendall(conn, request.encode('utf8')) # bytes
        print('Logging data: ', request)
    conn.close()
    print('Closing connection with: ', addr)


async def run_server():
    s = socket.socket(IPv4, TCP)
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on:', (HOST, PORT))
    s.setblocking(False) # configure socket in non-blocking mode

    loop = asyncio.get_event_loop()

    while True:
        conn, addr = await loop.sock_accept(s)
        print('Accepting connection from:', addr)
        loop.create_task(handle_client(conn, addr, loop))


try:
    asyncio.run(run_server())
except KeyboardInterrupt:
    print("Received KeyboardInterrupt, shutting down...")
    pass
