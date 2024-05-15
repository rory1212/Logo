import socket
from src.config.config import config
from src.utils.time import get_current_timestamp


def read_message(conn: socket.socket) -> str:
    max_length = config["log"]["max_length"]
    packet = conn.recv(max_length)
    if len(packet) == max_length:
        raise IOError(f"Payload is too big. Maximum length: {max_length}")
    if not packet:
        return ""
    return packet.decode().rstrip('\n')


def start_server(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server started on {host}:{port}")

        server_socket.listen()
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                try:
                    client_message = read_message(conn)
                    log_message = f"{get_current_timestamp()} {addr[0]}:{addr[1]} - {client_message}"
                    print("LOG:", log_message)
                    conn.sendall("ok".encode())
                except IOError as error:
                    conn.sendall(str(error).encode())


if __name__ == "__main__":
    server_config = config["server"]
    start_server(server_config["host"], server_config["port"])
