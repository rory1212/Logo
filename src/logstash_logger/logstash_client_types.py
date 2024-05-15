from typing import TypedDict


class LogstashLog(TypedDict):
    message: str
    ip: str
    port: int
