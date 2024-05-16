import socket
import threading
from typing import Any

from src.config.config import config
from src.log_message_parser import parse_log
from src.logstash_logger.logstash_client import LogstashClient


def read_message(conn: socket.socket) -> str:
    max_length = config["log"]["max_length"]
    packet = conn.recv(max_length)
    if len(packet) == max_length:
        raise IOError(f"Payload is too big. Maximum length: {max_length}")
    if not packet:
        return ""
    return packet.decode().rstrip('\n')


def handle_connection(conn: socket.socket, addr: Any, logstash: LogstashClient):
    with conn:
        print(f"{addr} Connected")
        while True:
            try:
                client_message = read_message(conn)
                parsed_log = parse_log(client_message, addr[0], addr[1])
                logstash.send_log(parsed_log["log"], parsed_log["logstash_overrides"])
                conn.sendall("ok".encode())
            except IOError as error:
                try:
                    conn.sendall(str(error).encode())
                except Exception as e:
                    print(f"{addr} Disconnected.", e)
                    break
            except Exception as e:
                print(f"{addr} Disconnected.", e)
                break


def start_server(host: str, port: int, logstash: LogstashClient) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server started on {host}:{port}")

        # To allow Ctrl+C KeyboardInterrupt, we need to release the "server_socket.accept()" occasionally
        server_socket.settimeout(5)
        server_socket.listen()
        while True:
            try:
                conn, addr = server_socket.accept()
            except socket.timeout:
                continue

            client_thread = threading.Thread(target=handle_connection, args=(conn, addr, logstash))
            client_thread.start()
