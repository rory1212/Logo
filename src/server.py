import socket
from src.config.config import config
from src.logstash_logger.logstash_client import LogstashClient


def read_message(conn: socket.socket) -> str:
    max_length = config["log"]["max_length"]
    packet = conn.recv(max_length)
    if len(packet) == max_length:
        raise IOError(f"Payload is too big. Maximum length: {max_length}")
    if not packet:
        return ""
    return packet.decode().rstrip('\n')


def start_server(host: str, port: int, logstash: LogstashClient) -> None:
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
                    logstash.send_log({"message": client_message, "ip": addr[0], "port": addr[1]})
                    conn.sendall("ok".encode())
                except IOError as error:
                    conn.sendall(str(error).encode())


def run():
    server_config = config["server"]
    logstash_config = config["logstash"]
    logstash_client = LogstashClient(logstash_config["host"], logstash_config["port"])
    logstash_client.connect()
    start_server(server_config["host"], server_config["port"], logstash_client)
    logstash_client.close()


if __name__ == "__main__":
    run()
