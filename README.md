# flask-todo-example
A simple RESTful application demo that uses Flask and Postgres to manage a to do list. Marshmallow is used for validating the REST request payloads. Scripts for setting up the database and testing the service are also provided.

## Database Model
The service uses a single database table with four fields:

```
item_id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY
description text NOT NULL
due_date timestamp
completed boolean NOT NULL
```

The unique item ids are generated on insert and autoincremented.  The description is a short description of the to do item.  To do items can optionally have a due date or null if none.  To do items must be marked as complete or incomplete -- on insertion, they are set to incomplete.

## REST API

```
POST /v1/todo

	Creates a to do item.  Expections a JSON payload with two fields ("description" and "due_date") with string values.  The due date is optional and should be given as a timestmap in ISO 8601 format.

	{
		"description" : "This is my to do item"
	}

	or 

	{
		"description" : "This is my to do item",
		"due_date" : "2023-03-07T18:34:09.157215" # Timestamp in 
	}

	Returns a JSON object with the field "item_id" (int) giving the id for the newly-created todo item.
```

```
GET /v1/todo

	Lists all current to do items.  No payload expected.
	
	Returns a JSON object with the field "todo_items" that maps to a list of JSON objects, one for each todo item.
```

```
GET /v1/todo/<int:item_id>

	Retrieves a single to do item, specified by the item_id  No payload expected.
	
	Returns a JSON object with four fields: item_id, description, due_date, and completed.
```

```
DELETE /v1/todo/<int:item_id>

	Deletes a single to do item, specified by the item_id  No payload expected.
	
	Returns a JSON object with the field "item_id" (int) giving the id for the deleted todo item.
```

```
PUT /v1/todo/<int:item_id>/mark_complete

	Sets a todo item's completed field to True. No payload expected.
	
	Returns a JSON object with the field "item_id" (int) giving the id for the effected todo item.
```

```
PUT /v1/todo/<int:item_id>/mark_incomplete

	Sets a todo item's completed field to False. No payload expected.
	
	Returns a JSON object with the field "item_id" (int) giving the id for the effected todo item.
```

```
PUT /v1/todo/<int:item_id>/due_date

	Sets a todo item's due_date field.  Expects a JSON payload with a single field (due_date).  The due date is either null or a timestmap string in ISO 8601 format.
	
	Returns a JSON object with the field "item_id" (int) giving the id for the effected todo item.
```
  

## Running
### Setup Database
The setup database will delete an existing database (if one exists), set up a new database and table, delete an existing role (if one exists), and set up a new role with the name `todo_service` and appropriate permissions.

```bash
$ POSTGRES_HOST=atlas POSTGRES_USER_PASSWORD=postgres POSTGRES_ADMIN_PASSWORD=postgres python3 setup_database.py
```

### Start Service
You can start the service from a terminal window. Leave the service running while you run the tests.
 
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -U pip wheel
$ pip install -r requirements.txt
$ POSTGRES_HOST=atlas POSTGRES_DATABASE=todo_application POSTGRES_USERNAME=todo_service POSTGRES_PASSWORD=postgres python todo_service.py
```



### Run Tests
The tests can be run in a separate terminal as follows:

```bash
$ source venv/bin/activate
$ BASE_URL=http://localhost:8000 python test_todo_service.py
```