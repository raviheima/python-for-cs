import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """Attempts to connect to a port on the given host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Timeout after 0.5 seconds
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def scan_ports(host, start=1, end=1000, max_threads=100):
    """Scans ports from start to end on the given host."""
    print(f"[*] Starting scan on host: {host} (ports {start}-{end})")
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for port in range(start, end + 1):
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    target_host = input("Enter target host (e.g., 192.168.1.1): ").strip()
    scan_ports(target_host)
