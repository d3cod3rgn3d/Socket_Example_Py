import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket()

    def start(self):
        try:
            # Bind the socket to the host and port
            self.socket.bind((self.host, self.port))

            # Listen for incoming connections, allowing up to 2 clients in the queue
            self.socket.listen(2)
            print(f"Server started on {self.host}:{self.port}")

            # Accept an incoming connection
            c, address = self.socket.accept()
            print(f"Connected to: {address}")

            while True:
                # Receive data from the client (up to 1024 bytes) and decode it
                data = c.recv(1024).decode()

                # If no data is received, break the loop
                if not data:
                    break
                print(f"Received from client: {data}")

                # Check if the received message is "bye"
                if data.strip().lower() == "bye":
                    # Send a confirmation message to the client
                    c.send(b"Server: Connection closed by server.")
                    # Close the connection
                    c.close()
                    print("Connection closed by server.")
                    break

                # Get user input and send it to the client after encoding
                response = input("Enter response to send to client: ")
                c.send(response.encode())
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Close the server socket
            self.socket.close()

if __name__ == "__main__":
    server = Server(socket.gethostname(), 21042)
    server.start()
