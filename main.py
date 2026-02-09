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
from fastapi import HTTPException
@app.post('/value', response_model=ChangeValueResponse)
async def change_value(req: ChangeValueRequest):
    result = await asyncio.to_thread(sync_inflation, req.region)

    try:
        return {"value": float(result)} 
    except Exception as e:
        raise HTTPException(500, detail=f"Gemini returns None -> {e}")
    except AttributeError as Attr:
        raise HTTPException(502, detail=f"Gemini returns None -> {Attr}")