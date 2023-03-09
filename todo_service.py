#!/usr/bin/env python

import datetime as dt
import os
import sys

from flask import Flask
from flask import request
from flask.json import jsonify

from marshmallow import fields
from marshmallow import post_load
from marshmallow import Schema
from marshmallow import ValidationError

import psycopg2
from psycopg2.extras import Json

DATABASE_KEY = "POSTGRES_DATABASE"
HOST_KEY = "POSTGRES_HOST"
USERNAME_KEY = "POSTGRES_USERNAME"
PASSWORD_KEY = "POSTGRES_PASSWORD"
PORT_KEY = "POSTGRES_PORT"
DEFAULT_PORT = 5432

app = Flask(__name__)

class TodoItem:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        
class TodoItemSchema(Schema):
    description = fields.String(required=True)
    due_date = fields.DateTime()
    
    @post_load
    def make_todo_item(self, data, **kwargs):
        return TodoItem(**data)
        
class DueDate:
    def __init__(self, due_date):
        self.due_date = due_date
        
class DueDateSchema(Schema):
    due_date = fields.DateTime(required=True, allow_none=True)
    
    @post_load
    def make_due_date(self, data, **kwargs):
        return DueDate(**data)

@app.route("/v1/todos", methods=["POST"])
def create_todo():
    payload = request.get_json()
    
    try:
        todo = TodoItemSchema().load(payload)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    uri = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get(USERNAME_KEY),
                                               os.environ.get(PASSWORD_KEY),
                                               os.environ.get(HOST_KEY),
                                               os.environ.get(PORT_KEY, DEFAULT_PORT),
                                               os.environ.get(DATABASE_KEY))

    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            query = "INSERT INTO todo_items (description, due_date, completed) VALUES (%s, %s, %s) " + \
                    "RETURNING item_id, description, due_date, completed;"
            cur.execute(query, (todo.description, todo.due_date, False))
            
            item_id, description, due_date, complete = cur.fetchone()

    conn.commit()
    conn.close()
    
    obj = {
        "item_id" : item_id,
        "description" : description,
        "due_date" : None if due_date is None else due_date.isoformat(),
        "complete" : complete
    }

    return jsonify(obj), 201
    
@app.route("/v1/todos", methods=["GET"])
def list_todos():
    uri = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get(USERNAME_KEY),
                                               os.environ.get(PASSWORD_KEY),
                                               os.environ.get(HOST_KEY),
                                               os.environ.get(PORT_KEY, DEFAULT_PORT),
                                               os.environ.get(DATABASE_KEY))

    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            query = "SELECT item_id, description, due_date, completed FROM todo_items;"
            cur.execute(query)
            
            todo_items = []
            for item_id, description, due_date, complete in cur.fetchall():
                item = {
                    "item_id" : item_id,
                    "description" : description,
                    "due_date" : None if due_date is None else due_date.isoformat(),
                    "complete" : complete
                }
                
                todo_items.append(item)

    conn.close()

    return jsonify({"todo_items" : todo_items}), 200
    
@app.route("/v1/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    uri = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get(USERNAME_KEY),
                                               os.environ.get(PASSWORD_KEY),
                                               os.environ.get(HOST_KEY),
                                               os.environ.get(PORT_KEY, DEFAULT_PORT),
                                               os.environ.get(DATABASE_KEY))

    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            query = "SELECT description, due_date, completed FROM todo_items " + \
                    "WHERE item_id = %s;"
            cur.execute(query, (todo_id, ))
            
            description, due_date, completed = cur.fetchone()

    conn.close()
    
    response = {
        "item_id" : todo_id,
        "description" : description,
        "due_date" : None if due_date is None else due_date.isoformat(),
        "complete" : completed
    }

    return jsonify(response), 200

@app.route("/v1/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    uri = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get(USERNAME_KEY),
                                               os.environ.get(PASSWORD_KEY),
                                               os.environ.get(HOST_KEY),
                                               os.environ.get(PORT_KEY, DEFAULT_PORT),
                                               os.environ.get(DATABASE_KEY))

    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            query = "DELETE FROM todo_items WHERE item_id = %s " + \
                    "RETURNING description, due_date, completed;"
            cur.execute(query, (todo_id, ))
            
            description, due_date, completed = cur.fetchone()

    conn.commit()
    conn.close()
    
    response = {
        "item_id" : todo_id,
        "description" : description,
        "due_date" : None if due_date is None else due_date.isoformat(),
        "complete" : completed
    }

    return jsonify(response), 200
    
@app.route("/v1/todos/<int:todo_id>/mark_complete", methods=["PUT"])
def mark_todo_complete(todo_id):
    uri = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get(USERNAME_KEY),
                                               os.environ.get(PASSWORD_KEY),
                                               os.environ.get(HOST_KEY),
                                               os.environ.get(PORT_KEY, DEFAULT_PORT),
                                               os.environ.get(DATABASE_KEY))

    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            query = "UPDATE todo_items SET completed = true WHERE item_id = %s " + \
                    "RETURNING description, due_date, completed;"
            cur.execute(query, (todo_id, ))
            
            description, due_date, completed = cur.fetchone()

    conn.commit()
    conn.close()
    
    response = {
        "item_id" : todo_id,
        "description" : description,
        "due_date" : None if due_date is None else due_date.isoformat(),
        "complete" : completed
    }

    return jsonify(response), 200

@app.route("/v1/todos/<int:todo_id>/mark_incomplete", methods=["PUT"])
def mark_todo_incomplete(todo_id):
    uri = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get(USERNAME_KEY),
                                               os.environ.get(PASSWORD_KEY),
                                               os.environ.get(HOST_KEY),
                                               os.environ.get(PORT_KEY, DEFAULT_PORT),
                                               os.environ.get(DATABASE_KEY))

    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            query = "UPDATE todo_items SET completed = false WHERE item_id = %s " + \
                    "RETURNING description, due_date, completed;"
            cur.execute(query, (todo_id, ))
            
            description, due_date, completed = cur.fetchone()

    conn.commit()
    conn.close()
    
    response = {
        "item_id" : todo_id,
        "description" : description,
        "due_date" : None if due_date is None else due_date.isoformat(),
        "complete" : completed
    }

    return jsonify(response), 200
    
@app.route("/v1/todos/<int:todo_id>/due_date", methods=["PUT"])
def set_todo_due_date(todo_id):
    payload = request.get_json()
    
    try:
        due_date = DueDateSchema().load(payload)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    uri = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get(USERNAME_KEY),
                                               os.environ.get(PASSWORD_KEY),
                                               os.environ.get(HOST_KEY),
                                               os.environ.get(PORT_KEY, DEFAULT_PORT),
                                               os.environ.get(DATABASE_KEY))

    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            query = "UPDATE todo_items SET due_date = %s WHERE item_id = %s " + \
                    "RETURNING description, due_date, completed;"
            cur.execute(query, (due_date.due_date, todo_id, ))
            
            description, due_date, completed = cur.fetchone()

    conn.commit()
    conn.close()
    
    response = {
        "item_id" : todo_id,
        "description" : description,
        "due_date" : None if due_date is None else due_date.isoformat(),
        "complete" : completed
    }

    return jsonify(response), 200


if __name__ == "__main__":
    if DATABASE_KEY not in os.environ or \
       HOST_KEY not in os.environ or \
       USERNAME_KEY not in os.environ or \
       PASSWORD_KEY not in os.environ:
        msg = "Must specify environmental variables {}, {}, {}, and {}.".format(DATABASE_KEY, HOST_KEY, USERNAME_KEY, PASSWORD_KEY)
        print(msg, file=sys.stderr)
        sys.exit(1)

    app.run(debug=True, host="localhost", port="8000")
