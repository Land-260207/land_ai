# 땅추출
import json
with open("util/land.json", "r") as f:
    data = json.load(f)

lands = [row["Column2"] for row in data["data"]]

# API호출
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def inflation():
    res = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = ''
    )

    return res