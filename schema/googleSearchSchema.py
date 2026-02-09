SCHEMA = {
    "type": "OBJECT",
    "required": ["delta_pp"],
    "properties": {
        "delta_pp": {
            "type": "NUMBER",
            "description": "price change in percentage points"
        }
    }
}

def getSchema():
    return SCHEMA