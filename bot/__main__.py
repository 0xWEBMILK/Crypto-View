# General modules
import asyncio

# Custom modules
from app import server



async def main():
    server.server_initialise()
    
    server.folders_initialise()
    server.handler_initialise()
    server.cors_initialise()

    server.run()



if __name__ == "__main__":
    asyncio.run(main())