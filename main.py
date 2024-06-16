import asyncio

import uvicorn

from run import app, background_tasks


async def main() -> None:
    """Create uvicorn server"""
    background_tasks()
    config = uvicorn.Config(app, port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
