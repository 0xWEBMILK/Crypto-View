# General modules
import asyncio

# Custom modules
from app import server



async def main():
    server.serverInitialise()
    server.foldersInitialise()
    server.handlerInitialise()

    server.run()



if __name__ == "__main__":
    asyncio.run(main())