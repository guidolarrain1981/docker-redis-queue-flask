# Flask & Redis Queue on Docker

Project that implements a Flask API & Redis Queue on Docker containers

Dashboard is included

### Requirements

- Docker (v:18.06.0+)
- Docker-Compose (v:1.13.0+)

### Usage

```sh
$ git clone https://github.com/guidolarrain1981/docker-redis-queue-flask.git
$ cd docker-redis-queue-flask
$ docker-compose up -d --build
```

## Table of ports
Service                  |  Host Port  | Container Port |
:-----------------------:|:-----------:|:---------------:
web                      | 5004 | 5000
flask-redis-queue_redis  |      | 6379
flask-redis-queue_worker |      |     
dashboard                | 9181 | 9181

### URLs

http://localhost:5004 [WEB]

http://localhost:9181 [DASHBOARD]

## Table of Endpoints
Name       |  Method  |  Usage  |
:---------:|:--------:|:--------:
tasks      |   POST   |   (1)   
tasks/ID   |   GET    |   (2)   
pop        |   POST   |   (3)   
push       |   POST   |   (4)   
count      |   GET    |   (5)   

```sh
(1) $ curl -F type=1 http://localhost:5004/tasks
(2) $ curl http://localhost:5004/tasks/<ID>
(3) $ curl -F type=1 http://localhost:5004/pop
(4) $ curl -F type=1 http://localhost:5004/push
(5) $ curl http://localhost:5004/count
```

### Monitoring

```sh
$ docker exec -it docker-redis-queue-flask_redis_1 redis-cli monitor
```

### Notes

This deploys a complete Redis Queue and Flask app plus a Dashboard using docker images based on https://github.com/mjhea0/flask-redis-queue
