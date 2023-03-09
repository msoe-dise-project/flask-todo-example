# Set the Due Date for a Todo Item
Set or remove the due date of an item

**URL** : `/v1/todo/:itemId/due_date`

**Method** : `PUT`

**Auth required** : NO

**Permissions required** : None

**Data constraints**: Expects a JSON payload with a single required field (due\_date).  The field's value must either be `null` (remove due date) or an ISO 8601-formatted date string.

**Data examples**:

```json
	{
		"due_date" : null
	}
```

	or 

```json
	{
		"due_date" : "2023-03-07T18:34:09.157215" # Timestamp in 
	}
```

## Success Response

**Condition** : If the item was found and the due date was formatted correctly

**Code** : `200 OK`

**Content example**

```json
{
		"item_id": 123,
		"description": "Run a load of laundry",
		"due_date" : "2023-03-07T18:34:09.157215",
		"complete" : true
}
```

## Error Response

**Condition** : If no todo item is found with that id

**Code** : `404 Not Found`

### Or

**Condition** : If the due date field was not `null` or a properly-formatted ISO 8601 timestamp string

**Code** : `400 Bad Request`