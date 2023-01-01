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


# flask commands
pip install flask
flask run
flask run --host 0.0.0.0
# db migrations commands
pip install flask-migrate
flask db init
flask db migrate  # takes the existing DB with the actual model to see if there are amy changes
flask db upgrade  # runs the upgrade function from the migration revision python file, same for flask db downgrade
# procedure when some data from models is changed
flask db migrate
