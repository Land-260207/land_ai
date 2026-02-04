from google import genai
import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def 
res = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = ''
)

return res