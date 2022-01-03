import socket
from utils import extract_json_data

# ASCII color codes
class bcolors:
    OKGREEN = '\033[92m'
    ENDCOL = '\033[0m'


class PortScan:

    # class vars
    IPv4 = socket.AF_INET # Internet address family
    TCP = socket.SOCK_STREAM # Socket type (protocol used to transport the message)
    PORTS_DATA_FILE = "./common_ports.json"

    # instance constructor
    def __init__(self):
        self.open_ports = []
        self.ports_info = {}
        self.remote_host = ""

    # class instance methods
    def get_ports_info(self):
        data = extract_json_data(PortScan.PORTS_DATA_FILE)
        self.ports_info = {int(k): v for (k, v) in data.items()}

    def scan_port(self, port):
        sock = socket.socket(PortScan.IPv4, PortScan.TCP)
        sock.settimeout(1.0)
        conn_status = sock.connect_ex((self.remote_host, port))
        if conn_status == 0:
            self.open_ports.append(port)
        sock.close()

    def run(self):
        print("Testing purpose only: use scanme.nmap.org ")
        target = input("Enter a web address: ")  # scanme.nmap.org
        self.remote_host = self.get_host_ip_addr(target)
        self.get_ports_info()
        for port in self.ports_info.keys():
            try:
                print(f"Scanning: {self.remote_host}:{port}")
                self.scan_port(port)
            except KeyboardInterrupt:
                print("\nExiting...")
                break

        print(f"{bcolors.OKGREEN}Found {self.open_ports.__len__()} open ports out of 698 in the common list.{bcolors.ENDCOL}")
        for port in self.open_ports:
            print(str(port), self.ports_info[port])

    # class static methods
    @staticmethod
    def get_host_ip_addr(target):
        try:
            ip_addr = socket.gethostbyname(target)
        except socket.gaierror as e:
            # Get Address Info Error
            print(f"Error... {e}")
        else:
            return ip_addr


if __name__ == "__main__":
    pscan = PortScan()
    pscan.run()
