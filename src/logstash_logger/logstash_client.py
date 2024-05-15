import socket
import json
from src.logstash_logger.logstash_client_types import LogstashLog


class LogstashClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_log(self, data: LogstashLog) -> None:
        if self.sock is None:
            raise Exception("Socket is not connected. Call connect() first.")
        log_message = json.dumps(data)
        self.sock.sendall((log_message + '\n').encode())

    def close(self) -> None:
        if self.sock is not None:
            self.sock.close()
            self.sock = None
