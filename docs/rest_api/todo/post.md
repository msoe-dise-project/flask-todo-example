# Create Todo Item
Creates a Todo item and assigns a unique id

**URL** : `/v1/todo`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : Expects a JSON payload with two fields ("description" and "due_date") with string values.  The due date is optional and should be given as a timestmap in ISO 8601 format.

```json
	{
			"description" : string,
			"due_date" : ISO 8601-formatted timestamp string
	}
```

**Data examples**:

```json
	{
		"description" : "This is my to do item"
	}
```

	or 

```json
	{
		"description" : "This is my to do item",
		"due_date" : "2023-03-07T18:34:09.157215" # Timestamp in 
	}
```

## Success Response

**Condition** : If everything is OK

**Code** : `201 CREATED`

**Content example**

```json
{
    "item_id": 123,
    "url": "http://testserver/v1/todo/123"
}
```

## Error Responses

**Condition** : If the description field is missing or the due\_date string is not formatted correctly.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "error": "The description field is required."
}
```