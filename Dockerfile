FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/djangoapp/src

COPY requirements.txt /opt/services/djangoapp/src/

RUN pip install -r /opt/services/djangoapp/src/requirements.txt

WORKDIR /opt/services/djangoapp/src

COPY . /opt/services/djangoapp/src

RUN pip install -U pip \
                   gunicorn
RUN apt-get update
RUN apt-get install -y vim

EXPOSE 8000
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "core", "core.wsgi:application"]
