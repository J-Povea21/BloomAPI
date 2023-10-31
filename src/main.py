# This is the main file of the application. Here we manage all the routes!

from fastapi import FastAPI
from bloom_filter import BloomFilter

app = FastAPI()

filter = BloomFilter(50, 0.05)


@app.get('/')
async def root():
    return {'status': True, 'message': 'API running...'}


@app.get("/bloom/add/{username}")
async def add(username: str):
    filter.add(username)
    return {'status': True, 'message': 'Username added!'}


@app.get("/bloom/check/{username}")
async def check(username: str):
    usernameExists = filter.check_existence(item=username)
    message = 'The username has been taken' if usernameExists else 'The username is available'
    return {'status': usernameExists, 'message': message}
