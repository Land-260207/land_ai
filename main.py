import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = 'hello'
)
print(response.text)

from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)