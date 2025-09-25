import socket

def scan_port(host, port):
    """Try to connect to a specific port and return True if open"""
    try:
        # Create a socket (like making a phone call)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Wait max 1 second for response
        
        # Try to connect (like knocking on the door)
        result = sock.connect_ex((host, port))
        sock.close()
        
        # If result is 0, connection succeeded (door is open)
        return result == 0
    except:
        return False

# Settings
host = 'localhost'  # Scan your own computer
start_port = 20
end_port = 50

print(f"Scanning ports {start_port}-{end_port} on {host}...")
print("Open ports:")

# Scan each port in the range
for port in range(start_port, end_port + 1):
    if scan_port(host, port):
        print(f"Port {port}: OPEN")

print("Scan complete!")