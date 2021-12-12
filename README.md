# Simple QRCode generator

![Screenshot](https://user-images.githubusercontent.com/20520161/145714467-053724a8-14f4-4202-a133-72285f07ae6f.png)

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
docker run -p 3000:3000 --env FG_COLOR="green" planeg/pwscapp:latest
```
