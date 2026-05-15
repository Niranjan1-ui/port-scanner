import socket
from concurrent.futures import ThreadPoolExecutor

TARGET = input("Enter target IP: ")


def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((TARGET, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()


print(f"Scanning target: {TARGET}")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1025))
