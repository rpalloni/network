# IP addresses as python objects

# IP address is an integer used to represent a host on a network
# network: group of IP address
# local network IP: hostname -I
# public network IP: curl ifconfig.me/ip

# IPv4 address is a 32-bit integer: 2^32 possible IPv4 from 0 to 4.294.967.295
# string with dot notation for easier use
(
    192 * (256 ** 3) + # octet (8 bit) = byte
    168 * (256 ** 2) +
      1 * (256 ** 1) +
    105 * (256 ** 0)
)

#    192    168    1     105
# |______|______|______|______|
#         network        host


# build an host address python object
from ipaddress import IPv4Address

addr = IPv4Address("192.168.1.105") # or IPv4Address(3232235881) or IPv4Address(b'\xc0\xa8\x01i')
addr
addr._ip

addr.packed
IPv4Address(b'\xc0\xa8\x01i')

# instances of IPv4Address are also hashable => keys in dict
num_connections = {
    hash(IPv4Address("192.168.1.105")): 2, # integer hashes from objects
    hash(IPv4Address("192.168.1.106")): 16,
    hash(IPv4Address("192.168.1.107")): 4,
}
num_connections


# build a network address python object
from ipaddress import IPv4Network
net = IPv4Network("192.168.1.0/24") # network IP + prefix [first 3 octets - 24 bits]
net.netmask # host + netmask = network

'''
host ip:    192.168.1.105 => 11000000 10101000 00000001 01101001
netmask ip: 255.255.255.0 => 11111111 11111111 11111111 00000000
                                192     168       1         0   => network ip

host ip:    192.168.1.103 => 11000000 10101000 00000001 01100111
netmask ip: 255.255.255.0 => 11111111 11111111 11111111 00000000
                                192     168       1         0   => network ip

two hosts in the same network
'''

net.broadcast_address # a single address to communicate to all the hosts on the network

addr in net # host is in the network

out_addr = IPv4Address("192.168.2.105")
out_addr in net # host is not in the network

net = IPv4Network("192.168.1.0/24")
net.num_addresses
for addr in net:
    print(addr)
