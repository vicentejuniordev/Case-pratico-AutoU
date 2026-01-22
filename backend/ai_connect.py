from google import genai
from google.genai import types
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def analisysAi(content):
    client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(system_instruction='Você é um assistente que analisa emails e os classifica em determinadas categorias que são: Produtivo: Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema) e Improdutivo: Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos). Além de analisar esses emails é preciso que você sugira uma resposta adequada para cada email analisado. Responda SOMENTE com JSON válido. Não use blocos ```json. Não inclua texto antes ou depois. sem explicações, no formato: {"categoria": "...", "resposta_sugerida": "..."}'),
        contents=content
    )
    
    return response.text


    