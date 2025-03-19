# Running
## Running a Postgres Database instance
If you have Docker installed, you can easily run an ephemeral Postgres instance:

```bash
$ docker run -d -e POSTGRES_PASSWORD=postgres --name postgres -p 5432:5432 docker.io/postgres:latest
```

## Setup Database
The setup database will delete an existing database (if one exists), set up a new database and table, delete an existing role (if one exists), and set up a new role with the name `todo_service` and appropriate permissions.

```bash
$ POSTGRES_HOST=localhost POSTGRES_USER_PASSWORD=postgres POSTGRES_ADMIN_PASSWORD=postgres python3 setup_database.py
```

## Start Service
You can start the service from a terminal window. Leave the service running while you run the tests.
 
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -U pip wheel
$ pip install -r requirements.txt
$ POSTGRES_HOST=localhost POSTGRES_DATABASE=todo_application POSTGRES_USERNAME=todo_service POSTGRES_PASSWORD=postgres flask --app app.todo_service:app run --host 0.0.0.0 --port 8000 --debug
```

## Run Tests
The tests can be run in a separate terminal as follows:

```bash
$ source venv/bin/activate
$ BASE_URL=http://localhost:8000 python test_todo_service.py
```
