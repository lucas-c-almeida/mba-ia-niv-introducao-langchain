# Ecossistema de serviços Langchain

## LangSmith
Plataforma paga online para observabilidade e debugging
- Monitoramento em produção
- Avaliação de performance de modelos
- Monitoramento de custos e latência

## LangServe
- APIs padronizadas para agentes.
- Servidores para deploy de aplicações langChain

## LangGraph
Framework para gerenciamento e orquestração de agentes de IA

## LangGraph Platform
Plataforma para gerenciamento dos agentes no framework de LangGraph. 

## LangGraph Studio
Interface para gerenciamento de projetos LangGraph. 

## LangChain Hub
Catálogo de artefatos da LangChain. 

É como um GitHub da langchain.

### Artefatos
- **Prompts**: Templates de prompts pré-definidos e reutilizáveis para interação com modelos de linguagem
- **Chains (Cadeias)**: Sequências de chamadas a modelos e ferramentas que automatizam fluxos de trabalho complexos
- **Agents (Agentes)**: Entidades que utilizam modelos de linguagem para tomar decisões e executar ações autônomas
- **Tools (Ferramentas)**: Componentes que estendem as capacidades dos agentes (buscas, cálculos, APIs externas, etc.)
- **Runnables**: Componentes executáveis que podem ser combinados em pipelines de processamento
- **Retrievers**: Componentes para recuperação de informações de bancos de dados vetoriais (RAG)

### Funções
- Publicação
- Versionamento
- Teste
- Download


# Funções do LangChain

Simplifica a integração com LLMs e serviços auxiliares.

- Contexto
- Busca semântica em vetores
- Roteadores

Pode ser utilizado em conjunto com outro framework. 

Abstrai a LLM. 

## Pacotes:
```python
import langchain-core
import langchain
import langchain-community #integrações extras

```

## LangChain Expressiona Language (LCEL)
Criação de Pipes ( | ).

Indicação de que a saída de uma ação é a entrada de outra ação. 


## Recursos Langchain
- **Runnables**: Células executaveis. Podem chamar modelos, processar dados, executar decisões, etc.
- **Criação de Chains**: Fluxos de execução de runnables. 
- **Carregamento de documentos**: Carrega documentos de fontes de dados diferentes. LangChain consegue carregar qualquer tipo de documento com um comando.
- **Divisão de Documentos**: Splitter. Seleciona trechos específicos ou divide o documento em chunks. 
- **Embedding**: Geração de embbedings com diversos provedores. 
- **Armazenamento Vetorial**: Armazena em diversos bancos (Pinecone, PGvector, Weaviate, FAISS)
- **Busca Semântica**
- **Memória**: Armazena o histórico de conversa
- **Templates de Prompts**
- **Placeholders em prompts**
- **Pydantic**: Definição de estruturas de classe. Os resultados da IA podem ser parseados em pydantic.
-**Sumarização**
-**Map-reduce de chamadas de IA**



## Métodos de Invocação do langchain_openai

O pacote `langchain_openai` fornece diferentes métodos para interagir com modelos de chat, cada um adequado para diferentes cenários:

### Métodos Síncronos

- **`invoke(input)`**: Execução síncrona única
  - Recebe uma entrada (string ou mensagem)
  - Retorna um objeto `AIMessage` completo com `.content`
  - Bloqueia até receber a resposta completa
  - Uso: Chamadas simples e diretas

- **`stream(input)`**: Streaming síncrono
  - Retorna um iterador que produz chunks (tokens) conforme são gerados
  - Cada chunk é um objeto com `.content`
  - Útil para exibir respostas em tempo real
  - Uso: Quando você quer ver a resposta sendo gerada token por token

- **`batch(inputs)`**: Processamento em lote síncrono
  - Recebe uma lista de entradas
  - Processa múltiplas requisições de uma vez
  - Retorna lista de resultados na mesma ordem das entradas
  - Uso: Quando você tem várias requisições e quer processá-las juntas

### Métodos Assíncronos

- **`ainvoke(input)`**: Execução assíncrona única
  - Versão assíncrona do `invoke()`
  - Deve ser usado com `await` dentro de funções `async`
  - Não bloqueia a execução
  - Uso: Chamadas únicas em código assíncrono

- **`astream(input)`**: Streaming assíncrono
  - Versão assíncrona do `stream()`
  - Retorna um async iterator
  - Deve ser usado com `async for`
  - Uso: Streaming em aplicações assíncronas

- **`abatch(inputs)`**: Processamento em lote assíncrono
  - Versão assíncrona do `batch()`
  - Processa múltiplas requisições em paralelo de forma assíncrona
  - Mais eficiente que múltiplos `ainvoke()` com `asyncio.gather()`
  - Uso: Múltiplas requisições em paralelo (recomendado para performance)

### Tabela Comparativa

| Método | Tipo | Entrada | Retorno | Quando Usar |
|--------|------|---------|---------|-------------|
| `invoke()` | Síncrono | 1 entrada | Objeto completo | Chamada única simples |
| `stream()` | Síncrono | 1 entrada | Iterador de chunks | Resposta em tempo real |
| `batch()` | Síncrono | Lista de entradas | Lista de objetos | Várias requisições, código síncrono |
| `ainvoke()` | Assíncrono | 1 entrada | Objeto completo (await) | Chamada única em código async |
| `astream()` | Assíncrono | 1 entrada | Async iterator | Streaming em apps async |
| `abatch()` | Assíncrono | Lista de entradas | Lista de objetos (await) | Múltiplas requisições em paralelo |

### Exemplos de Uso

**invoke()**:
```python
message = model.invoke("Hello World")
print(message.content)
```

**stream()**:
```python
for chunk in model.stream("Hello World"):
    print(chunk.content, end="", flush=True)
```

**batch()**:
```python
inputs = ["Pergunta 1", "Pergunta 2", "Pergunta 3"]
results = model.batch(inputs)
for result in results:
    print(result.content)
```

**ainvoke()**:
```python
result = await model.ainvoke("Hello World")
print(result.content)
```

**abatch()**:
```python
inputs = ["Pergunta 1", "Pergunta 2", "Pergunta 3"]
results = await model.abatch(inputs)
for result in results:
    print(result.content)
```

### Classes Principais do langchain_openai

- **`ChatOpenAI`**: Modelos de chat (GPT-3.5, GPT-4, etc.) - suporta todos os métodos acima
- **`OpenAI`**: Modelos de linguagem tradicionais (legacy)
- **`OpenAIEmbeddings`**: Geração de embeddings vetoriais para busca semântica
- **`OpenAIImageGenerator`**: Geração de imagens com DALL·E

Todos esses métodos seguem o padrão **Runnable** do LangChain, permitindo composição com pipes (`|`) e integração em chains complexas.


# Gerenciamento de API Keys no LangChain

## Autenticação Automática via Variáveis de Ambiente

O LangChain **não requer** passar API keys explicitamente no código. Ele lê automaticamente as chaves das variáveis de ambiente usando nomes padrão específicos para cada provedor.

**Variáveis de Ambiente Padrão**:
   - `OPENAI_API_KEY` - Para modelos OpenAI (ChatOpenAI, OpenAIEmbeddings, etc.)
   - `GOOGLE_API_KEY` - Para modelos Google Gemini
   - Outros provedores seguem padrões similares

**Carregamento via `.env`**:
   ```python
   from dotenv import load_dotenv
   load_dotenv()  # Carrega variáveis do arquivo .env
   
   # Não precisa passar API key explicitamente!
   model = ChatOpenAI(model="gpt-5-nano")
   gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
   ```

### Passagem Explícita (Opcional)

Se necessário, pode passar explicitamente:
```python
import os
from dotenv import load_dotenv
load_dotenv()

# Opção 1: Automático (recomendado)
model = ChatOpenAI(model="gpt-5-nano")

# Opção 2: Explícito (quando necessário)
model = ChatOpenAI(
    model="gpt-5-nano",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

# Arquitetura Básica do LangChain

**Ponto de atenção**: *langchain evolui muito rápido, então rapidamente componentes ficam legados ou até mesmo deprecados. **Sempre verificar a versão do langchain sendo utilizada.** Tomar cuidado com a sugestão de IA no desenvolvimento, porque os agentes podem estar considerando uma versão antiga.*


