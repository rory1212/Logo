from typing import TypedDict


class ServerConfig(TypedDict):
    host: str
    port: int


class LogConfig(TypedDict):
    max_length: int


class Config(TypedDict):
    server: ServerConfig
    log: LogConfig
