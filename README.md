# aiohttp_mongo Project

## Description
This project is an aiohttp API using mongodb.

## Run server
Run server without database (does not work when database is needed)
```console
python -m venv venv
pip install -r requirements.txt
python server.py
```

## Run docker containers
```console
docker-compose build
docker-compose run
```

## Docker images
The server image is available on Docker Hub:
https://hub.docker.com/repository/docker/piermarquis/web_app

The mongodb image is hosted on Bitnami registry.

