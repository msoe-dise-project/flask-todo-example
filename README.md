# flask-todo-example
A simple RESTful service demo that uses Flask and Postgres to manage a to do list. Marshmallow is used for validating the REST request payloads. Scripts for setting up the database and testing the service are also provided.

## Running the Service

The service can be run with Docker compose like so:

```bash
$ docker compose build --no-cache
$ docker compose up -d
[+] Building 0.0s (0/0)
[+] Running 4/4
 ✔ Network flask-todo-example_default  Created                                                                    0.1s
 ✔ Container postgres                  Healthy                                                                    6.8s
 ✔ Container database-setup            Exited                                                                     6.7s
 ✔ Container todo-service              Started                                                                    7.0s
```

You can then check the status of the containers like so:

```bash
$ docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS                    PORTS                                       NAMES
ca73d6061f0f   todo-service        "/bin/sh -c 'flask r…"   12 seconds ago   Up 5 seconds (healthy)    0.0.0.0:8888->8888/tcp, :::8888->8888/tcp   todo-service
dddc6d6d8a8c   postgres:bullseye   "docker-entrypoint.s…"   12 seconds ago   Up 12 seconds (healthy)   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   postgres
```

Both containers should have a status of "healthy".  If you see "health: starting", wait a minute and query the status again.

## Documentation

* [Database schema](docs/database_schema.md)
* [REST API](docs/rest_api/README.md)
* [Running the service and tests](docs/running.md)

## License

Unless otherwise noted, the source files are distributed
under the Apache Version 2.0 license found in the LICENSE file.
