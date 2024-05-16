import json
from typing import TypedDict

from src.config.config_types import ServerConfig
from src.logstash_logger.logstash_client_types import LogstashLog


class ParsedLog(TypedDict):
    log: LogstashLog
    logstash_overrides: ServerConfig | None


def parse_log(message: str, ip: str, port: int) -> ParsedLog:
    res: ParsedLog = {"log": {"ip": ip, "port": port}, "logstash_overrides": None}
    try:
        data = json.loads(message)
        if "logstash" in data:
            res["logstash_overrides"] = data["logstash"]
            res["logstash_overrides"]["port"] = int(res["logstash_overrides"]["port"])
            del data["logstash"]
        if "body" in data:
            res["log"] = {**res["log"], **data["body"]}
    except json.JSONDecodeError:
        res["log"]["message"] = message

    return res
