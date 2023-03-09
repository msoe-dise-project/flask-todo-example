# List Todo Items
Lists all todo items

**URL** : `/v1/todo`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**: No payload expected.

## Success Response

**Condition** : If everything is OK

**Code** : `200 OK`

**Content example**

```json
{
	"todo_items": [
	 	{
			"item_id": 123,
			"description": "Run a load of laundry",
			"due_date" : "2023-03-07T18:34:09.157215",
			"complete" : false
		}
	]
}
```