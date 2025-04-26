# https://github.com/RichardHan/mssql_mcp_server
# Create server parameters for stdio connection

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
import asyncio

model = ChatOllama(
    model="cogito",
    system="You're a helpful assistant that can answer questions about a SQL Server database. You can also execute SQL queries and return the results.",)

#Reference your local MCP server
server_params = StdioServerParameters(
    command="python",
    args=["sql_server.py"],
)

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": 
            #"Give me the products in table Products started with the letter b in description?"
            "List all products in table Products"
            })

            # Extrair e imprimir o conteúdo da última resposta do agente
            if isinstance(agent_response, dict) and "messages" in agent_response:
                for msg in reversed(agent_response["messages"]):
                    if msg.__class__.__name__ == "AIMessage" and msg.content:
                        return msg.content

# Run the async function
if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(result)