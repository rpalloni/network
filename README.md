# network
A network is a group of IP addresses. \
Network configuration for each host (device) depends on the ip and subnet mask => network ip

# socket
A socket is the software component to enable the communication between processes working on two physically separate machines. 
From an application point of view, it is a particular object on which to read and write the data to be transmitted or received. 
~~~
a socket is the 'standard interface' to connect common 
electronic devices to the home electric network

    SOCKET         PLUG
     _____        _______
____|     |>>>>  | _ | _ |
____|     |      ||_|||_||
    |_____|>>>>  |___|___|
~~~
 

# Berkeley sockets API (standard socket functions):
### * set up the listening socket: listens for connections from clients
socket() \
bind() \
listen() \
accept() // server accepts client connection \
connect() // client establishes connection \
_The three-way handshake is important since it ensures that each side of the connection is reachable in the network,
in other words that the client can reach the server and vice-versa. 
It may be that only one host, client or server, can reach the other._

### * exchanging data
send() \
recv()

### * close respective sockets
close()

![tcp-socket-flow](https://user-images.githubusercontent.com/17080117/147975429-3615c769-ca89-45a3-90c0-324b24c08d82.png)

