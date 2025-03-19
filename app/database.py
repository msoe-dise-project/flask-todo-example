# We create a separate database module so that the same ConnectionPool
# object is shared across multiple worker threads.
# See: https://www.psycopg.org/psycopg3/docs/advanced/pool.html#other-ways-to-create-a-pool
# See: https://stackoverflow.com/questions/55523299/best-practices-for-persistent-database-connections-in-python-when-using-flask 

import atexit
import os
import sys

import psycopg
from psycopg_pool import ConnectionPool

DATABASE_KEY = "POSTGRES_DATABASE"
HOST_KEY = "POSTGRES_HOST"
USERNAME_KEY = "POSTGRES_USERNAME"
PASSWORD_KEY = "POSTGRES_PASSWORD"
PORT_KEY = "POSTGRES_PORT"
DEFAULT_PORT = 5432

def check_env():
    if DATABASE_KEY not in os.environ or \
           HOST_KEY not in os.environ or \
           USERNAME_KEY not in os.environ or \
           PASSWORD_KEY not in os.environ:
            msg = "Must specify environmental variables {}, {}, {}, and {}.".format(DATABASE_KEY, HOST_KEY, USERNAME_KEY, PASSWORD_KEY)
            print(msg, file=sys.stderr)
            sys.exit(1)

uri = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get(USERNAME_KEY),
                                           os.environ.get(PASSWORD_KEY),
                                           os.environ.get(HOST_KEY),
                                           os.environ.get(PORT_KEY, DEFAULT_PORT),
                                           os.environ.get(DATABASE_KEY))

pool = ConnectionPool(uri, open=True)

atexit.register(pool.close)
