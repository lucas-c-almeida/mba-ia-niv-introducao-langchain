from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
load_dotenv()

long_text = """
Dawn threads a pale gold through the alley of glass.
The city yawns in a chorus of brakes and distant sirens.
Windows blink awake, one by one, like sleepy eyes.
Streetcloth of steam curls from manholes, a quiet river.
Coffee steam spirals above a newspaper's pale print.
Pedestrians sketch light on sidewalks, hurried, loud with umbrellas.
Buses swallow the morning with their loud yawns.
A sparrow perches on a steel beam, surveying the grid.
The subway sighs somewhere underground, a heartbeat rising.
Neon still glows in the corners where night refused to retire.
A cyclist cuts through the chorus, bright with chrome and momentum.
The city clears its throat, the air turning a little less electric.
Shoes hiss on concrete, a thousand small verbs of arriving.
Dawn keeps its promises in the quiet rhythm of a waking metropolis.
The morning light cascades through towering windows of steel and glass,
casting geometric shadows on busy streets below.
Traffic flows like rivers of metal and light,
while pedestrians weave through crosswalks with purpose.
Coffee shops exhale warmth and the aroma of fresh bread,
as commuters clutch their cups like talismans against the cold.
Street vendors call out in a symphony of languages,
their voices mixing with the distant hum of construction.
Pigeons dance between the feet of hurried workers,
finding crumbs of breakfast pastries on concrete sidewalks.
The city breathes in rhythm with a million heartbeats,
each person carrying dreams and deadlines in equal measure.
Skyscrapers reach toward clouds that drift like cotton,
while far below, subway trains rumble through tunnels.
This urban orchestra plays from dawn until dusk,
a endless song of ambition, struggle, and hope.
"""

# RecursiveCharacterTextSplitter separa o texto priorizando o corte nas quebras 
# (pontuação, parágrafo ou espaço)
# É possível indicar separadores 

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, # Quantos caracteres cada chunk deve ter (aproximadamente)
    chunk_overlap=70    # Insere trachos repetidos anteriores e seguintes nos chunks
                        # Evita perda de contexto no corte.
)

parts = splitter.create_documents([long_text])
# A função create_documents gera uma lista de Documents
# Os documents podem ser inseridos como Runnables

# Imprimir exemplo
for part in parts:
    print(part.page_content)
    print("-"*30)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

chain_summarize = load_summarize_chain(llm, chain_type="stuff", verbose=False)

result = chain_summarize.invoke({"input_documents": parts})
# Retorna um dicionário contendo:
# - input_documents: os documentos fornecidos
# - output_text: resumo

# A chain do tipo "stuff" junta todos os 
print(result["output_text"])