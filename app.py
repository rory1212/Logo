from src.args_parser import parse_args
from src.config.config import config
from src.logstash_logger.logstash_client import LogstashClient
from src.server import start_server


def update_config():
    args = parse_args()
    logstash_config = config["logstash"]
    if args.ip is not None:
        logstash_config["host"] = args.ip
    if args.port is not None:
        logstash_config["port"] = args.port


if __name__ == "__main__":
    update_config()
    server_config = config["server"]
    logstash_config = config["logstash"]

    logstash_client = LogstashClient(logstash_config["host"], logstash_config["port"])
    logstash_client.connect()

    start_server(server_config["host"], server_config["port"], logstash_client)

    logstash_client.close()
