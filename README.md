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
