# Django REST Application

# Project Requirements (If run with docker)

1. Docker & Docker-compose
2. Python 3.7
3. Git

# Project Setup
1. Firstly clone the project

    `git clone https://github.com/mkawsar/django-rest-api.git`
2. Goto the project root directory and copy the environment file following the command

    `cp .env.example .env`
3. Run the docker following the command

    `docker-composer up --build -d`
4. After the completed check the docker container list

    `docker ps`
5.  Goto the django rest app with the docker container

    1. `docker exec -it {app containter ID or Name} bash`
    2. Collect the static files

        `python manage.py collectstatic --no-input`
    3. Updated the config/db/database_env to .env file with database credentials
    4. Migrate the database

        `python manage.py migrate`
    5. Insert the users from database seeder

        `python manage.py add_user`
6. Finally run the project with the following url

    `http://0.0.0.0:8000/`

# Project setup (With virtual environment)

1. Firstly clone the project

    `git clone https://github.com/mkawsar/django-rest-api.git`
2. Goto the project root directory and copy the environment file following the command

    `cp .env.example .env`

	1. Update the postgres database name, host, username, password and schema name or public schema
3. Install the python dependencies following the command

	`pip install -r requirements.txt`

4. Migrate the database

    `python manage.py migrate`
5. Added users from migrate command

	`python manage.py add_user`

6. Finally run the local server
	`python manage.py runserver`


