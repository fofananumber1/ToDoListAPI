To-Do List API
Author: Salif Fofana
Version: 1.0

Desc:
This is To-Do List API, a simple API that allows the user to create, obtain, update, and delete tasks. 

Steps to run locally:

1. Clone the repo.
2. Create a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `uvicorn main:app --reload`

Known Issues

Currently, the POST /tasks/ endpoint returns "Not Found". Debugging in progress.