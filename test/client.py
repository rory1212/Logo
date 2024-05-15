import socket

PORT = 65432


def start_client(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        try:
            while True:
                message = input("Enter message to send (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    print("Closing connection...")
                    break

                client_socket.sendall(message.encode())
                response = client_socket.recv(1024)
                print(f"Received from server: {response.decode()}")
        except KeyboardInterrupt:
            print("\nClient interrupted and closing connection...")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    start_client("127.0.0.1", PORT)
