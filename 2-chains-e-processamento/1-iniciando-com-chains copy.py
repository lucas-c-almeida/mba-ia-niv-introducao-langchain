from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

question_template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name!"
)

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

chain = question_template | model #O output de question template é o input de model

result = chain.invoke({"name": "Wesley"}) # Parâmetros vão para o question_template
print(result.content)

# Esta é apenas uma forma de criar as chains.
# Os próximos arquivos mostram outras formas.