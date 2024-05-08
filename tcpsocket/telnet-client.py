import socket

HOST = '127.0.0.1'
PORT = 7007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    
    # Send message to server
    message = "Hello Coding Challenges!\n"
    client_socket.sendall(message.encode())
    
    # Receive response from server
    response = client_socket.recv(1024)
    print(f"Received: {response.decode()}")