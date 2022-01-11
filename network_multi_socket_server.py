# handle multiple connections
import socket
import asyncio

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65413       # Port to listen on (non-privileged ports are > 1023)
IPv4 = socket.AF_INET # Internet address family
TCP = socket.SOCK_STREAM # Socket type (protocol used to transport the message)


async def handle_client(conn):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(conn, 255)).decode('utf8')
        await loop.sock_sendall(conn, request.encode('utf8'))
        print('Logging data: ', request)
    conn.close()

async def run_server():
    s = socket.socket(IPv4, TCP)
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on', (HOST, PORT))
    s.setblocking(False) # configure socket in non-blocking mode

    loop = asyncio.get_event_loop()

    while True:
        conn, addr = await loop.sock_accept(s)
        print('Accepted connection from', addr)
        loop.create_task(handle_client(conn))

asyncio.run(run_server())