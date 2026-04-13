from fastmcp import FastMCP
from database.db import init_db
import mcp_app.tools_voiture as tools_voitures
import asyncio

mcp_server = FastMCP("Automobiles MCP Server")
tools_voitures.register_tools(mcp_server)

async def main():
    # Init DB avant le lancement du serveur
    await init_db()
    print(" MongoDB connecté")

    # Lancer le serveur (bloquant)
    await mcp_server.run_async(
        transport="streamable-http",
        host="127.0.0.1",
        port=8002,
        path="/mcp",
    )

if __name__ == "__main__":
    asyncio.run(main())