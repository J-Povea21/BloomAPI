# This is the main file of the application. Here we manage all the routes!

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bloom_filter import BloomFilter

# API config
app = FastAPI()
origins = ['http://localhost:3000']

app.add_middleware(CORSMiddleware,
                   allow_origins = origins,
                   allow_credentials = True,
                   allow_methods = ['*'],
                   allow_headers = ['*']
                   )


# Bloom filter object
filter = BloomFilter(50, 0.05)


@app.get('/')
async def root():
    return {'status': True, 'message': 'API running...'}


@app.get("/bloom/add/{username}")
async def add(username: str):
    usernameExists = filter.check_existence(username)

    if usernameExists:
        return {'status': False, 'message': 'The username is already taken (probably)'}
    else:
        filter.add(username)
        return {'status': True, 'message': 'Username added!'}

