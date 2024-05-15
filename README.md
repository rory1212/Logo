# Logo
In Log We Trust

## Pre-Installations
1. Python 3.12.3

## Run
### Local Developing
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
gunicorn --reload --bind 127.0.0.1:65432 src.wsgi:run
```

## Deploy
- Install docker
- `docker-compose up`
- Link to local [Kibana](http://localhost:5601) (port 5601)
- 

## Work process
### Tools used
Client testing tool - [client.py](external_sources/client/client.py) (Run: `python external_sources/client/client.py`)

## Assumptions
- Log message maximum length is 4096 (configurable). To avoid creation of protocol between client and server.
- The timestamp is added automatically.
