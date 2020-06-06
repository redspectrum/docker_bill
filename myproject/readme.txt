
From here:
https://ruddra.com/posts/docker-do-stuff-using-celery-using-redis-as-broker/


add static
docker exec DJANGOXDOCKERNAME /bin/sh -c "python manage.py collectstatic --noinput"


docker-compose build
docker-compose up -d (reload)
docker-compose run

docker-compose stop
docker-compose start

docker-compose logs db
docker-compose logs nginx
docker-compose logs web
===================

All is done. Now lets run docker-compose build in terminal within the project directory. It will build/rebuild(if necessary) all the containers. For first time running the containers, run docker-compose up -d. Lets go to browser and type: localhost:8000. We should see the django application up and running.
Start and stop docker compose

For stopping the docker, run docker-compose stop. Re-running docker, use docker-compose start.
https://ruddra.com/posts/docker-django-nginx-postgres/
==================
To use this project, run this commands:

    make up to build the project and starting containers.
    make build to build the project.
    make start to start containers if project has been up already.
    make stop to stop containers.
    make shell-web to shell access web container.
    make shell-db to shell access db container.
    make shell-nginx to shell access nginx container.
    make logs-web to log access web container.
    make logs-db to log access db container.
    make logs-nginx to log access nginx container.
    make collectstatic to put static files in static directory.
    make log-web to log access web container.
    make log-db to log access db container.
    make log-nginx to log access nginx container.
    make restart to restart containers.

===================

Run:
docker-compose up -d --build

Open by local:
http://0.0.0.0:8000/

Check postgresql in settings
docker stop $(docker ps -a -q)


docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser



