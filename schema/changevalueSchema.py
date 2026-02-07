from pydantic import BaseModel

class ChangeValueRequest(BaseModel):
    region: str

class ChangeValueResponse(BaseModel):
    delta_pp: float