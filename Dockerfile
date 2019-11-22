FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir -p code/
COPY requirements.txt code/

RUN pip install --no-cache-dir -r code/requirements.txt

WORKDIR /code

COPY . /code

RUN pip install -U pip \
                   gunicorn
RUN apt-get update
RUN apt-get install -y vim

EXPOSE 8000
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "core", "core.wsgi:application"]