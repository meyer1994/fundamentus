from fastapi import FastAPI

import fundamentus

app = FastAPI()

data = fundamentus.load()


@app.get('/')
async def get():
    return data
