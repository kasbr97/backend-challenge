# backend-challenge Getting started

First you must have python installed and pip to install the dependencies in the requirements.txt file.
`pip install -r /path/to/requirements.txt`

For the database on this project, I used MySQL Workbench so the String on .env.example is specially for it. Create a schema in MySQL workbench and then create a .env file fill the attributes according to the example file.

### Running the program

While being in the /backend-challenge folder run the command
`uvicorn app.main:app --reload`

This will start the backend API and you can go to the link that shows in the commandline to check.
Once running, you can go to the URL + /docs endpoint to check the User endpoint more easily.
