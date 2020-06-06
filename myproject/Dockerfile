FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /config
ADD /config/requirements.pip /config/
RUN pip install -r /config/requirements.pip
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn mydjango.wsgi -b 0.0.0.0:8000 & celery worker --app=myapp.tasks