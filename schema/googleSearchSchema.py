SCHEMA = {
    "type": "OBJECT",
    "required": ["delta_pp", "news_titles"],
    "properties": {
        "delta_pp": {
            "type": "NUMBER",
            "description": "price change in percentage points"
        },
        "news_titles": {
            "type": "ARRAY",
            "items": {"type": "STRING"}
        }
    }
}

def getSchema():
    return SCHEMA