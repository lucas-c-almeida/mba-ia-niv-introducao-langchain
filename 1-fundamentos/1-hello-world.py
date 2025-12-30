import asyncio
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
message = model.invoke("Hello World")

print(message.content)

# Adicionado um exemplo de stream.
for chunk in model.stream("Hello World"):
    print(chunk.content, end="", flush=True)

# Adicionando exemplo de ainvoke (Assíncrono)
async def main():
    model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
    
    # Cria múltiplas tarefas assíncronas
    tasks = [
        model.ainvoke("O que é Python?"),
        model.ainvoke("Explique machine learning"),
        model.ainvoke("Conte uma piada")
    ]
    
    # Executa todas em paralelo
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result.content)
        print("-" * 40)

asyncio.run(main())