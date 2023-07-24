# How to run a project in windows

> python -m venv p-env

## Activate the env

> cd p-env/Scripts
> activate
> cd ../..

## Upgrade the pip

> python -m pip install --upgrade pip

## Install requirements

> pip install -r requirements.txt


## Run the app.py file

> python app.py



# How to run test cases

> pytest tests.py



# API Details

## Hello world

GET http://127.0.0.1:5000

## Health check

GET http://127.0.0.1:5000/api/v1/health-check

## create user

POST http://127.0.0.1:5000/api/v1/users

{
    "name": "Narendra",
    "email":"narendra_test@gmail.com",
    "age": 26
}

## get users

GET http://127.0.0.1:5000/api/v1/users

## get user

http://127.0.0.1:5000/api/v1/users/1

## update user

PUT http://127.0.0.1:5000/api/v1/users/1

{
    "name": "Narendra",
    "email":"narendra_test@gmail.com",
    "age": 26,
    "status": false
}

## delete user

DELETE http://127.0.0.1:5000/api/v1/users/3

## get blob properties size

GET http://127.0.0.1:5000/api/v1/blob/properties