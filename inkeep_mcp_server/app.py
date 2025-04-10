from fastapi import FastAPI

from inkeep_mcp_server.server import mcp

app = FastAPI()

app.mount("/", mcp.sse_app())
