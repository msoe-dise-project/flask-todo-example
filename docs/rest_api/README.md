# REST API

## Todo Item-Related

* [Create todo item](todo/post.md) : `POST /v1/todo`
* [List todo items](todo/get.md) : `GET /v1/todo`
* [Get todo item](todo/itemId/get.md) : `GET /v1/todo/:itemId`
* [Delete todo item](todo/itemId/delete.md) : `DELETE /v1/todo/:itemId`
* [Mark todo item complete](todo/itemId/mark_complete/put.md) : `PUT /v1/todo/:itemId/mark_complete`
* [Mark todo item incomplete](todo/itemId/mark_incomplete/put.md) : `PUT /v1/todo/<int:item_id>/mark_incomplete`
* [Set todo item due date](todo/itemId/due_date/put.md) : `PUT /v1/todo/<int:item_id>/due_date`

## Metrics

* [Get current application metrics](metrics/get.md) : `GET /metrics`

## Healthcheck

* [Perform healthcheck](healthcheck/get.md) : `GET /healthcheck`

The file system layout and endpoint templates follow the examples provided by [@iros](https://gist.github.com/iros/3426278) and [@jamescooke](https://github.com/jamescooke/restapidocs).

