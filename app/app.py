from fastapi import FastAPI

app = FastAPI()

# minimal app - get request
@app.get('/', tags=['ROOT'])
async def root() -> dict:
	return {
		"message": "Hello FastAPI"
	}

# Get ---> Read Todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict :
	return {
		'data': todos
	}

# Post ---> Create todo
@app.post('/todo', tags=['todos'])
async def add_todo(todo: dict) -> dict :
	todos.append(todo)
	return {
		'message': 'A todo has been added'
	}

# Put --> Update todo
@app.put('/todo/{id}', tags=['todos'])
async def update_todo(id: int, body: dict) -> dict :
	for todo in todos :
		if todo['id'] == id :
			todo['Activity'] = body['Activity']
			return {
				"message": f'Todo with id {id} has been updated'
			}

	return {
		'message': f'Todo with this id number {id} was not found!'
	}


@app.delete('/todo{id}', tags=['todos'])
async def delete_todo(id: int) -> dict :
	for todo in todos :
		if todo['id'] == id :
			# todos.remove(todo)
			del todos[id - 1]
			return {
				'message': f'Todo with id {id} has been deleted'
			}
	
	return {
		'message': f'Todo with this id number {id} was not found!'
	}

todos = [
	{
		'id': 1,
		'activity': 'Jogging for 2 hours at 7:00 AM'
	},
	{
		'id': 2,
		'Activity': 'Writing 3 pages of my new book at 2:00 PM'
	}
]