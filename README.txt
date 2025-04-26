Projeto: Agente SQL Server com LangGraph, MCP e Ollama

Este projeto permite interagir com uma base de dados SQL Server usando um agente inteligente construído com LangGraph e ferramentas MCP, alimentado por um modelo local Ollama.
A interação é feita através de uma interface gráfica simples em Gradio.

---

Funcionalidades:
- Consultar tabelas e dados de uma base de dados SQL Server.
- Executar consultas SQL diretamente via agente.
- Utilizar um modelo local (Ollama Llama 3.1) para interpretar perguntas em linguagem natural.
- Interface gráfica pronta em Gradio.
- Arquitetura baseada em MCP para comunicação cliente-servidor via stdio.

---

Tecnologias Utilizadas:
- Python 3.11+
- Gradio
- LangGraph
- Ollama
- pymssql
- MCP Framework

---

Instalação:
1. Clonar o repositório
2. Instalar dependências com `pip install -r requirements.txt`
3. Criar um ficheiro .env com configurações da base de dados

---

Execução:
- Corre `python client2.py`
