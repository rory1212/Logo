import socket
from config import config


def start_server(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server started on {host}:{port}")

        server_socket.listen()
        print("Waiting for a connection...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                print(f"Received: {data.decode()}")
                conn.sendall(data)


if __name__ == "__main__":
    server_config = config["server"]
    start_server(server_config["host"], server_config["port"])
