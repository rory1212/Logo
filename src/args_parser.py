import argparse
from argparse import Namespace


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="set logstash IP")
    parser.add_argument("--port", help="set logstash port")
    args = parser.parse_args()
    return args
