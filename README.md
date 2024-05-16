# Logo
In Log We Trust

#### By Joseph Drachinsky

## Pre-Installations
1. Python 3.12.3
2. Docker

## Run
### Local Developing
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Deploy
- `docker-compose up --build`
- Link to local [Kibana](http://localhost:5601) (port 5601)
#### All services are online! 

## Messages Logo types
- Text message. Will log inside "message" field
- JSON. Logo can receive JSONs. Fields:
  - body - full body of the log. Can contain any field.
  - logstash
    - host - override the ip configuration
    - port - override the port configuration
  - example:
  ```json
  {
    "body": {
      "message": "Hello World!",
      "count": 6
    },
    "logstash": {
      "host": "localhost",
      "port": "5044"
    }
  }
  ```

## Work process
### Tools used
Client testing tool - [client.py](external_sources/client/client.py) (Run: `python external_sources/client/client.py`)

### Assumptions
- Log message maximum length is 4096 (configurable). To avoid creation of protocol between client and server.
- The timestamp is added automatically.
- You can configure the ip/port of the centralized log service from the arguments. (See `python app.py --help`)

### Main Tasks
- [X] Logo Listen to incoming connections on port TCP/1313.
- [X] Logo is capable of serving multiple clients concurrently. Each sending one request (log message) at a time.
- [X] Logo adds the current timestamp and client's IP to every log.
- [X] Then Logo passes all the log messages to a logstash.
- [X] The IP address and TCP port number of logstash are configurable.
- [X] Logo is always up and running, ready to serve new messages on any failure - Logo is always on and never stops.
