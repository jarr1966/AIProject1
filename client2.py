import gradio as gr
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

# Inicializar modelo
model = ChatOllama(
    model="llama3.1",
    system=(
        "You're a helpful assistant that can answer questions about a SQL Server database."
        "You can also execute SQL queries and return the results."
        "Products are in table 'Products' with columns: code, description, price, stock."
        "Clients are in table 'Clients' with columns: code, name, city, sales."
    )
)

# Configuração do servidor MCP
server_params = StdioServerParameters(
    command="python",
    args=["sql_server.py"]
)

# Função principal assíncrona para interagir com o agente
async def run_agent(user_input):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            response = await agent.ainvoke({"messages": user_input})

            if isinstance(response, dict) and "messages" in response:
                for msg in reversed(response["messages"]):
                    if msg.__class__.__name__ == "AIMessage" and msg.content:
                        return msg.content
            return "Sem resposta do agente."

# Wrapper síncrono para integração com Gradio
def ask_agent(message):
    try:
        return asyncio.run(run_agent(message))
    except Exception as e:
        return f"Erro ao processar a pergunta: {e}"

# Interface gráfica com Gradio
with gr.Blocks(title="Agente SQL com LangGraph + MCP + Ollama") as iface:
    gr.Markdown("""
        # 🧠 Agente SQL com LangGraph + MCP + Ollama
        Escreve uma pergunta sobre a base de dados SQL Server. O agente utiliza ferramentas MCP e LangGraph com um modelo local.
    """)

    with gr.Row():
        txt_input = gr.Textbox(label="Pergunta", placeholder="Ex: Lista todos os produtos da tabela Products")
    with gr.Row():
        btn_submit = gr.Button("Perguntar")
    with gr.Row():
        txt_output = gr.Textbox(label="Resposta", lines=10)

    btn_submit.click(fn=ask_agent, inputs=txt_input, outputs=txt_output)

if __name__ == "__main__":
    iface.launch()
