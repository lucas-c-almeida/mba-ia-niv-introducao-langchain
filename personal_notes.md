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



# Arquitetura Básica do LangChain

**Ponto de atenção**: *langchain evolui muito rápido, então rapidamente componentes ficam legados ou até mesmo deprecados. **Sempre verificar a versão do langchain sendo utilizada.** Tomar cuidado com a sugestão de IA no desenvolvimento, porque os agentes podem estar considerando uma versão antiga.*


