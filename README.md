# Simple QRCode generator

## Running locally

```bash
#git clone ...
#cd <clone dir>
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd app
uwsgi --ini uwsgi.ini
```

By default it runs on 0.0.0.0:3000

## Run in a docker contianer

[DockerHub](https://hub.docker.com/repository/docker/planeg/pwscapp)

```
docker run planeg/pwscapp:latest
```
