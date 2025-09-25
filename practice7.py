import socket

# Create a socket (think of it as a phone)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up the address (IP and port)
host = 'localhost'  # Your computer
port = 9999

# Bind the socket to the address (assign the phone number)
server_socket.bind((host, port))

# Start listening for connections (wait for calls)
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

try:
    while True:
        # Accept a connection (answer the phone)
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        
        # Receive data from client (listen to what they say)
        data = client_socket.recv(1024).decode('utf-8')
        
        if data:
            print(f"Received: {data}")
            # Echo the data back (repeat what they said)
            client_socket.send(data.encode('utf-8'))
        
        # Close the connection (hang up)
        client_socket.close()

except KeyboardInterrupt:
    print("\nServer shutting down...")
finally:
    server_socket.close()