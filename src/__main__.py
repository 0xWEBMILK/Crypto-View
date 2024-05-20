# General modules
import asyncio

# Custom modules
from app import server



async def main():
    server.handlerInitializate()
    server.run()



if __name__ == "__main__":
    asyncio.run(main())