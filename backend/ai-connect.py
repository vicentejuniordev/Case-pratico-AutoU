from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

async def analisysAi(content):
    client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(system_instruction='Você apenas responde em português.'),
        contents=content
    )
    
    return response.text

    