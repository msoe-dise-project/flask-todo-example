# Mark a Todo Item as Complete
Marks a single todo item as complete

**URL** : `/v1/todo/:itemId/mark_complete`

**Method** : `PUT`

**Auth required** : NO

**Permissions required** : None

**Data constraints**: No payload expected.

## Success Response

**Condition** : If the item was found

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