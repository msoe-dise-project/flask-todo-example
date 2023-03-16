# Perform Healthcheck
Performs a healthcheck by verifying that the database can be reached and the main table exists.

**URL** : `/healthcheck`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**: No payload expected.

## Success Response

**Condition** : If everything is OK

**Code** : `200 OK`

**Content example**

```
	{
		"database" :
		{
			"healthy" : True
		}
	}
```

## Error Response

**Condition** : If there is a failure of any type

**Code** : `500 Internal Server Failure`
