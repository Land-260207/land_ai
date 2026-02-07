from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

from schema.changevalueSchema import ChangeValueRequest, ChangeValueResponse
from util.changevalue import sync_inflation
app = FastAPI(docs_url='/api', redoc_url='/api/redoc', openapi_url='/openapi.json')

@app.get('/health')
def Health():
    return {'status': 'ok good best'}

import asyncio
@app.post('/value', response_model=ChangeValueResponse)
async def change_value(req: ChangeValueRequest):
    result = await asyncio.to_thread(sync_inflation, req.region)
    return result