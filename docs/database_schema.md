# Database Schema
The service uses a single database table with four fields:

```
item_id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY
description text NOT NULL
due_date timestamp
completed boolean NOT NULL
```

The unique item ids are generated on insert and autoincremented.  The description is a short description of the to do item.  To do items can optionally have a due date or null if none.  To do items must be marked as complete or incomplete -- on insertion, they are set to incomplete.