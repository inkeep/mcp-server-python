# mcp-server-python
Inkeep MCP Server for your docs!

### Dependencies

- An account on [Inkeep](https://inkeep.com)
- [`uv`](https://github.com/astral-sh/uv)

### Setup

```
git clone git@github.com:inkeep/mcp-server-python.git
cd mcp-server-python
uv venv
uv pip install -r pyproject.toml
```

You'll need these environment variables:
```
INKEEP_API_BASE_URL=https://api.inkeep.com/v1
INKEEP_API_KEY=
INKEEP_API_MODEL=inkeep-rag-20250310
```
To get an API key, go to the Inkeep Portal and create an API Integration.


### `claude_desktop_config.json`

```
{
    "mcpServers": {
        "your-docs-by-inkeep-mcp-server": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-server-python",
                "run",
                "-m",
                "inkeep_mcp_server"
            ],
            "env": {
                "INKEEP_API_BASE_URL": "https://api.inkeep.com/v1",
                "INKEEP_API_KEY": "YOUR_INKEEP_API_KEY",
                "INKEEP_API_MODEL": "inkeep-rag-20250310"
            }
        },
    }
}
```

You may need to put the full path to the `uv` executable in the command field. You can get this by running `which uv` on MacOS/Linux or `where uv` on Windows.
