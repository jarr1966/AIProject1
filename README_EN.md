# 🧠 SQL Server Agent with LangGraph, MCP, and Ollama

This project allows interaction with a SQL Server database through an intelligent agent combining LangGraph, MCP Tools, and the local Ollama model (Llama 3.1).
A user-friendly interface is provided using Gradio for natural language interaction.

---

## 🚀 Features

- Browse tables and data from a SQL Server database.
- Execute SQL queries using natural language.
- Gradio-based graphical interface.
- Client-server communication via MCP (stdio protocol).

---

## 📁 Project Structure

- `client2.py` — Client that creates the Gradio interface and integrates LangGraph + MCP + Ollama.
- `sql_server.py` — MCP server exposing the SQL Server database as tools and resources.

---

## 🛠️ Technologies Used

- Python 3.11+
- Gradio
- LangGraph
- LangChain
- Ollama (Llama3.1 model)
- pymssql
- MCP Framework
- dotenv

---

## ⚙️ Installation

```bash
git clone <REPOSITORY_URL>
cd <PROJECT_FOLDER>
pip install -r requirements.txt
```

Create a `.env` file with the following variables:
```
MSSQL_SERVER=localhost
MSSQL_USER=sa
MSSQL_PWD=your_secure_password
MSSQL_DATABASE=ERP
```

---

## 🚦 How to Run

```bash
python client.py
```

The Gradio web interface will open for you to ask questions about your database.

---

## 📝 Example Questions

- List all products from the Products table
- How many clients are located in Lisbon?
- What is the price of the product with code 1001?

---

## ⚠️ Notes

- Ollama must be installed locally, with the `llama3.1` model available.
- Database credentials are loaded through the `.env` file.
- Ensure that TCP/IP connections are enabled in your SQL Server configuration.

---

## 📄 License

No explicit license. Please credit **Jose Ribeiro** if you reuse this project.

---
