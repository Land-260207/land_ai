# 땅추출
import json
with open("util/land.json", "r", encoding='utf-8') as f:
    data = json.load(f)["data"]

land = [row for row in data if isinstance(row.get('※ 매월 말일자 통계 현황'), str) and row['※ 매월 말일자 통계 현황'].isdigit() and len(row['※ 매월 말일자 통계 현황']) == 10 and row['※ 매월 말일자 통계 현황'].endswith('000000') and not row['※ 매월 말일자 통계 현황'].endswith('00000000')]
lands = [row["Column2"] for row in land]
print(len(lands))

# API호출
from google import genai
from schema.googleSearchSchema import getSchema
from util.prompt import getPrompt
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
SCHEMA = getSchema()

from google.genai import types
grounding_tool = types.Tool(google_search=types.GoogleSearch())

def sync_inflation(region: str):
    PROMPT = getPrompt(region = lands)
    config = types.GenerateContentConfig(
        tools=[grounding_tool],
        temperature=0.1,
    )
    res = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=PROMPT,
        config=config,
    )

    return res.text