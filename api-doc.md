## Endpoints:

### `GET /tasks`

Returns a list of tasks.

```
> GET /tasks

< 200 OK
{
  tasks: Task[] = [
    { id: number, label: string, completed: boolean }
  ]
}
```

### `POST /tasks`

Creates a new task.

```
> POST /tasks
{ label: string }

< 201 Created
{
  task: { id: number, label: string, completed: boolean }
}
```

### `POST /tasks/:id`

Updates the task of the given ID.

```
> POST /tasks/:id
{ label: string } |
{ completed: boolean } |
{ label: string, completed: boolean }

< 200 OK
{
  task: Task = { id: number, label: string, completed: boolean }
}

< 404 Not Found
{ error: string }
```

### `DELETE /tasks/:id`

Deletes the task of the given ID.

```
> DELETE /tasks/:id

< 200 OK

< 404 Not Found
{ error: string }
```

### Subtasks:
### `GET /tasks/:id/subtasks`

Returns a list of subtasks of task :id

```
> GET /tasks/:id/tasks

< 200 OK
{
  tasks: Task[] = [
    { id: number, label: string, completed: boolean }
  ]
}
```

### `POST /tasks/:id/subtasks`

Creates a new subtask of task :id

```
> POST /tasks
{ label: string }

< 201 Created
{
  task: { id: number, label: string, completed: boolean }
}
```