'''
port scanning: test a server in order to understand which ports are listening on a specific machine 
'''
import socket

# ASCII color codes
class bcolors:
    OKGREEN = '\033[92m'
    KORED = '\033[91m'
    ENDCOL = '\033[0m'


IPv4 = socket.AF_INET # Internet address family
TCP = socket.SOCK_STREAM # Socket type (protocol used to transport the message)

OPEN_PORTS = []
CLOSED_PORTS = []

def scan_port(ip, port):
    sock = socket.socket(IPv4, TCP)
    sock.settimeout(1.0)
    conn_status = sock.connect_ex((ip, port))
    # 0: conn ok, 1: conn ko
    if conn_status == 0:
        OPEN_PORTS.append(port)
    else:
        CLOSED_PORTS.append(port)
    sock.close()

def get_host_ip_addr(target):
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror as e:
        # Get Address Info Error
        print(f"Error... {e}")
    else:
        return ip_addr


if __name__ == "__main__":
    print("Testing purpose only: use scanme.nmap.org ")
    target = input("Enter a web address: ") # scanme.nmap.org
    ip_addr = get_host_ip_addr(target)
    while True:
        try:
            port = int(input("Enter a port: ")) # 80 (http), 22 (ssh), 21 (ftp), 25 (smtp), 443 (encrypt)
            scan_port(ip_addr, port)
            print(f"{bcolors.OKGREEN}Open ports list: {OPEN_PORTS}{bcolors.ENDCOL} \n{bcolors.KORED}Closed ports list: {CLOSED_PORTS}{bcolors.ENDCOL}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
