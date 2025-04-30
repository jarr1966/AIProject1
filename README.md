# 🧠 Agente SQL Server com LangGraph, MCP e Ollama

Este projeto permite interagir com uma base de dados SQL Server através de um agente inteligente que combina LangGraph, MCP Tools e o modelo local Ollama (Llama 3.1).
A interface gráfica é fornecida por Gradio para facilitar a interação em linguagem natural.

---

## 🚀 Funcionalidades

- Consultar tabelas e dados de uma base de dados SQL Server.
- Executar queries SQL usando linguagem natural.
- Interface gráfica com Gradio.
- Comunicação cliente-servidor via MCP (usando stdio).

---

## 📁 Estrutura do Projeto

- `client2.py` — Cliente que cria a interface Gradio e integra LangGraph + MCP + Ollama.
- `sql_server.py` — Servidor MCP que expõe a base de dados SQL Server como ferramentas e recursos.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Gradio
- LangGraph
- LangChain
- Ollama (modelo Llama3.1)
- pymssql
- MCP Framework
- dotenv

---

## ⚙️ Instalação

```bash
git clone <URL_DO_REPOSITÓRIO>
cd <PASTA_DO_PROJETO>
pip install -r requirements.txt
```

Criar um `.env`:
```
MSSQL_SERVER=localhost
MSSQL_USER=sa
MSSQL_PWD=senha_segura
MSSQL_DATABASE=ERP
```

---

## 🚦 Como Executar

```bash
python client.py
```

---

## 📝 Exemplos de Perguntas

- Lista todos os produtos da tabela Products
- Quantos clientes existem na cidade de Lisboa?
- Qual o preço do produto com o código 1001?

---

## ⚠️ Notas

- Necessário ter o Ollama instalado com o modelo llama3.1.
- As credenciais da base de dados são lidas via .env.

---

## 📄 Licença

Sem licença explícita. Por favor creditar o autor em caso de reutilização.
