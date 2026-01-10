"""
Init chat model é uma maneira mais agnóstica de fazer a implementação. 
Não necessita de um objeto específico para o modelo.
O modelo escolhido é selecionado via variável model_provider
"""

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
answer_gemini = gemini.invoke("Hello World")
print(answer_gemini.content)