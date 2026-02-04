from fastapi import FastAPI
import os
from dotenv import load_dotenv
from schema.ChangeValue import ChangeValueRequest, ChangeValueResponse

load_dotenv()
app = FastAPI(docs_url='/api', redoc_url='/api/redoc', openapi_url='/openapi.json')

@app.get('/health')
def Health():
    return {'status': 'ok good best'}

@app.post('/value', response_model = ChangeValueResponse)
async def change_value(req: ChangeValueRequest):
    pass