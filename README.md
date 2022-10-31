# Coding All Stars

### Requirements

- Python 3.8+
- Docker and Docker-compose (optional)

## Installation
### Using Docker

- Create `.env` file and copy variable from .env.sample
- Build and run the container
 -- For the first run, below command will automatically build image and run the container
  ```
  docker-compose up 
  ```
  -- If you wannt a new build and run the container just run the command below
  ```
  docker-compose build
  docker-compose up 
  docker-compose up -d # for demaon mode
  ```
### You can also pull docker image directly and run it
- Pull image
```
docker pull premanuj/coding-allstars:0.0.1
```
- Run image
```
docker run premanuj/coding-allstars:0.0.1
```
### Without docker
- Activate an virtutia env
  ``` 
  source venv/bin/activate
  ```
- install requirements
  ```
  pip install -r requirements.txt
  ```
- Create .env file and copy variable from .env.sample
- Run application
  ```
  python manage.py runserver
  ```
  NOTE: You can user run.sh to run the application which will collect all static file and server file through gunicorn for that just change the permission by following:
  ```
  chmod +x run.sh
  ```
  and then just run the command below.
  ```
  ./run.sh
  ```