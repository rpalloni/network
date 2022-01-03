import json
import socket

# ASCII color codes
class bcolors:
    OKGREEN = '\033[92m'
    ENDCOL = '\033[0m'

IPv4 = socket.AF_INET # Internet address family
TCP = socket.SOCK_STREAM # Socket type (protocol used to transport the message)

OPEN_PORTS = []
PORTS_DATA_FILE = "./common_ports.json" # port:most-common-service


def extract_json_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def get_ports_info():
    data = extract_json_data(PORTS_DATA_FILE)
    ports_info = {int(k): v for (k, v) in data.items()} # convert port number to int
    return ports_info

def get_host_ip_addr(target):
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror as e:
        # Get Address Info Error
        print(f"Error... {e}")
    else:
        return ip_addr

def scan_port(ip, port):
    sock = socket.socket(IPv4, TCP)
    sock.settimeout(1.0)
    conn_status = sock.connect_ex((ip, port))
    if conn_status == 0:
        OPEN_PORTS.append(port)
    sock.close()


if __name__ == "__main__":
    print("Testing purpose only: use scanme.nmap.org ")
    target = input("Enter a web address: ")  # scanme.nmap.org
    ip_addr = get_host_ip_addr(target)
    ports_info = get_ports_info()

    for port in ports_info.keys():
        try:
            print(f"Scanning: {ip_addr}:{port}")
            scan_port(ip_addr, port)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

    print(f"{bcolors.OKGREEN}Found {OPEN_PORTS.__len__()} open ports out of 698 in the common list.{bcolors.ENDCOL}")
    for port in OPEN_PORTS:
        print(str(port), ports_info[port])
