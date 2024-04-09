import socket

def client():
    try:
        # Get the host name (as both server and client code are running on your PC)
        host = socket.gethostname()

        # Define the server's port number to interact with
        port = 21042

        # Create a socket object
        client_socket = socket.socket()

        # Connect to the server by specifying the hostname and port number
        client_socket.connect((host, port))

        # Prompt the user for input
        message = input("Enter your message (Type 'bye' to exit): ")
        while message.lower().strip() != "bye":
            if message.lower().strip() == "exit":
                # If user types "exit", close the socket and exit the loop
                client_socket.close()
                print("Connection closed by client.")
                break

            # Send the message to the server
            client_socket.send(message.encode())
            # Receive a response from the server
            data = client_socket.recv(1024).decode()
            # Display the received message from the server
            print("Received from server: " + data)
            # Prompt for the next message
            message = input("Enter your message (Type 'bye' to exit): ")

        # Close the connection
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    client()
