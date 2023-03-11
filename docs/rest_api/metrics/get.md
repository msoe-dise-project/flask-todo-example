# Get Current Metric Values
Returns metrics computed using the [Prometheus Python](https://github.com/prometheus/client_python) library.  In addition to the basic Python garbage collection metrics, the following are implemented:

* Number of requests recieved, by type (see `requests_total`)
* Response times, by type (see `response_times_bucket`)

**URL** : `/metrics`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**: No payload expected.

## Success Response

**Condition** : If everything is OK

**Code** : `200 OK`

**Content example**

```
	# HELP python_gc_objects_collected_total Objects collected during gc
	# TYPE python_gc_objects_collected_total counter
	python_gc_objects_collected_total{generation="0"} 1378.0
	python_gc_objects_collected_total{generation="1"} 41.0
	python_gc_objects_collected_total{generation="2"} 0.0
	# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
	# TYPE python_gc_objects_uncollectable_total counter
	python_gc_objects_uncollectable_total{generation="0"} 0.0
	python_gc_objects_uncollectable_total{generation="1"} 0.0
	python_gc_objects_uncollectable_total{generation="2"} 0.0
	# HELP python_gc_collections_total Number of times this generation was collected
	# TYPE python_gc_collections_total counter
	python_gc_collections_total{generation="0"} 84.0
	python_gc_collections_total{generation="1"} 7.0
	python_gc_collections_total{generation="2"} 0.0
	# HELP python_info Python platform information
	# TYPE python_info gauge
	python_info{implementation="CPython",major="3",minor="11",patchlevel="1",version="3.11.1"} 1.0
	# HELP requests_total Number of Requests Received
	# TYPE requests_total counter
	requests_total{request_type="post::todos"} 11.0
	requests_total{request_type="get::todos"} 3.0
	requests_total{request_type="delete::todos::todoId"} 1.0
	requests_total{request_type="get::todos::todoId"} 5.0
	requests_total{request_type="put::todos::todoId::mark_complete"} 1.0
	requests_total{request_type="put::todos::todoId::mark_incomplete"} 1.0
	requests_total{request_type="put::todos::todoId::due_date"} 1.0
	# HELP requests_created Number of Requests Received
	# TYPE requests_created gauge
	requests_created{request_type="post::todos"} 1.678499589892511e+09
	requests_created{request_type="get::todos"} 1.678499589957182e+09
	requests_created{request_type="delete::todos::todoId"} 1.6784995900011609e+09
	requests_created{request_type="get::todos::todoId"} 1.678499590118189e+09
	requests_created{request_type="put::todos::todoId::mark_complete"} 1.678499590564126e+09
	requests_created{request_type="put::todos::todoId::mark_incomplete"} 1.678499590706038e+09
	requests_created{request_type="put::todos::todoId::due_date"} 1.6784995908714418e+09
	# HELP response_times Distribution of Request Times
	# TYPE response_times histogram
	response_times_bucket{le="0.005",request_type="post::todos"} 0.0
	response_times_bucket{le="0.01",request_type="post::todos"} 0.0
	response_times_bucket{le="0.025",request_type="post::todos"} 0.0
	response_times_bucket{le="0.05",request_type="post::todos"} 9.0
	response_times_bucket{le="0.075",request_type="post::todos"} 11.0
	response_times_bucket{le="0.1",request_type="post::todos"} 11.0
	response_times_bucket{le="0.25",request_type="post::todos"} 11.0
	response_times_bucket{le="0.5",request_type="post::todos"} 11.0
	response_times_bucket{le="0.75",request_type="post::todos"} 11.0
	response_times_bucket{le="1.0",request_type="post::todos"} 11.0
	response_times_bucket{le="2.5",request_type="post::todos"} 11.0
	response_times_bucket{le="5.0",request_type="post::todos"} 11.0
	response_times_bucket{le="7.5",request_type="post::todos"} 11.0
	response_times_bucket{le="10.0",request_type="post::todos"} 11.0
	response_times_bucket{le="+Inf",request_type="post::todos"} 11.0
	response_times_count{request_type="post::todos"} 11.0
	response_times_sum{request_type="post::todos"} 0.4667195832589641
	response_times_bucket{le="0.005",request_type="get::todos"} 0.0
	response_times_bucket{le="0.01",request_type="get::todos"} 0.0
	response_times_bucket{le="0.025",request_type="get::todos"} 0.0
	response_times_bucket{le="0.05",request_type="get::todos"} 2.0
	response_times_bucket{le="0.075",request_type="get::todos"} 3.0
	response_times_bucket{le="0.1",request_type="get::todos"} 3.0
	response_times_bucket{le="0.25",request_type="get::todos"} 3.0
	response_times_bucket{le="0.5",request_type="get::todos"} 3.0
	response_times_bucket{le="0.75",request_type="get::todos"} 3.0
	response_times_bucket{le="1.0",request_type="get::todos"} 3.0
	response_times_bucket{le="2.5",request_type="get::todos"} 3.0
	response_times_bucket{le="5.0",request_type="get::todos"} 3.0
	response_times_bucket{le="7.5",request_type="get::todos"} 3.0
	response_times_bucket{le="10.0",request_type="get::todos"} 3.0
	response_times_bucket{le="+Inf",request_type="get::todos"} 3.0
	response_times_count{request_type="get::todos"} 3.0
	response_times_sum{request_type="get::todos"} 0.14772904198616743
	response_times_bucket{le="0.005",request_type="get::todos::todoId"} 0.0
	response_times_bucket{le="0.01",request_type="get::todos::todoId"} 0.0
	response_times_bucket{le="0.025",request_type="get::todos::todoId"} 0.0
	response_times_bucket{le="0.05",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="0.075",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="0.1",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="0.25",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="0.5",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="0.75",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="1.0",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="2.5",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="5.0",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="7.5",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="10.0",request_type="get::todos::todoId"} 5.0
	response_times_bucket{le="+Inf",request_type="get::todos::todoId"} 5.0
	response_times_count{request_type="get::todos::todoId"} 5.0
	response_times_sum{request_type="get::todos::todoId"} 0.18458508409094065
	response_times_bucket{le="0.005",request_type="delete::todos::todoId"} 0.0
	response_times_bucket{le="0.01",request_type="delete::todos::todoId"} 0.0
	response_times_bucket{le="0.025",request_type="delete::todos::todoId"} 0.0
	response_times_bucket{le="0.05",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="0.075",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="0.1",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="0.25",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="0.5",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="0.75",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="1.0",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="2.5",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="5.0",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="7.5",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="10.0",request_type="delete::todos::todoId"} 1.0
	response_times_bucket{le="+Inf",request_type="delete::todos::todoId"} 1.0
	response_times_count{request_type="delete::todos::todoId"} 1.0
	response_times_sum{request_type="delete::todos::todoId"} 0.03420408407691866
	response_times_bucket{le="0.005",request_type="put::todos::todoId::mark_complete"} 0.0
	response_times_bucket{le="0.01",request_type="put::todos::todoId::mark_complete"} 0.0
	response_times_bucket{le="0.025",request_type="put::todos::todoId::mark_complete"} 0.0
	response_times_bucket{le="0.05",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="0.075",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="0.1",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="0.25",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="0.5",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="0.75",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="1.0",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="2.5",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="5.0",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="7.5",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="10.0",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_bucket{le="+Inf",request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_count{request_type="put::todos::todoId::mark_complete"} 1.0
	response_times_sum{request_type="put::todos::todoId::mark_complete"} 0.039594125002622604
	response_times_bucket{le="0.005",request_type="put::todos::todoId::mark_incomplete"} 0.0
	response_times_bucket{le="0.01",request_type="put::todos::todoId::mark_incomplete"} 0.0
	response_times_bucket{le="0.025",request_type="put::todos::todoId::mark_incomplete"} 0.0
	response_times_bucket{le="0.05",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="0.075",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="0.1",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="0.25",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="0.5",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="0.75",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="1.0",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="2.5",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="5.0",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="7.5",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="10.0",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_bucket{le="+Inf",request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_count{request_type="put::todos::todoId::mark_incomplete"} 1.0
	response_times_sum{request_type="put::todos::todoId::mark_incomplete"} 0.03615995799191296
	response_times_bucket{le="0.005",request_type="put::todos::todoId::due_date"} 0.0
	response_times_bucket{le="0.01",request_type="put::todos::todoId::due_date"} 0.0
	response_times_bucket{le="0.025",request_type="put::todos::todoId::due_date"} 0.0
	response_times_bucket{le="0.05",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="0.075",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="0.1",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="0.25",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="0.5",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="0.75",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="1.0",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="2.5",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="5.0",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="7.5",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="10.0",request_type="put::todos::todoId::due_date"} 1.0
	response_times_bucket{le="+Inf",request_type="put::todos::todoId::due_date"} 1.0
	response_times_count{request_type="put::todos::todoId::due_date"} 1.0
	response_times_sum{request_type="put::todos::todoId::due_date"} 0.038016209029592574
	# HELP response_times_created Distribution of Request Times
	# TYPE response_times_created gauge
	response_times_created{request_type="post::todos"} 1.67849958910411e+09
	response_times_created{request_type="get::todos"} 1.6784995891043499e+09
	response_times_created{request_type="get::todos::todoId"} 1.678499589104536e+09
	response_times_created{request_type="delete::todos::todoId"} 1.678499589104836e+09
	response_times_created{request_type="put::todos::todoId::mark_complete"} 1.678499589105072e+09
	response_times_created{request_type="put::todos::todoId::mark_incomplete"} 1.678499589105315e+09
	response_times_created{request_type="put::todos::todoId::due_date"} 1.678499589105559e+09
```