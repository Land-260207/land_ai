from pydantic import BaseModel

class ChangeValueRequest(BaseModel):
    curValue: float

class ChangeValueResponse(BaseModel):
    value: float