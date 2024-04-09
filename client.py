import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket()

    def connect(self):
        try:
            # Connect to the server by specifying the hostname and port number
            self.socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")

            # Prompt the user for input
            message = input("Enter your message (Type 'bye' to exit): ")
            while message.lower().strip() != "bye":
                if message.lower().strip() == "exit":
                    # If user types "exit", close the socket and exit the loop
                    self.socket.close()
                    print("Connection closed by client.")
                    return

                # Send the message to the server
                self.socket.send(message.encode())
                # Receive a response from the server
                data = self.socket.recv(1024).decode()
                # Display the received message from the server
                print("Received from server: " + data)
                # Prompt for the next message
                message = input("Enter your message (Type 'bye' to exit): ")

            # Close the connection
            self.socket.close()
            print("Connection closed by client.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    client = Client('127.0.0.1', 33000)
    client.connect()
