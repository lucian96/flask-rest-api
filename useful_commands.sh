#!/bin/bash
# basic commands
docker image ls; docker container ls [-a]; docker start container_id; docker stop container_id;
docker network ls; docker network inspect network_id;

# for building the image
docker build -t rest-api-flask-python .

# for debugging into the container
docker run -it rest-api-flask-python /bin/bash

# for running a container with exposed port 5005, mapped to 5000 and mapped external volume
docker run -d -p 5005:5000 -w /app -v "$(pwd):/app" rest-api-flask-python
