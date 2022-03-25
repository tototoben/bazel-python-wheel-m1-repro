import asyncio
import asyncpg


print("heheh")

async def main():
    conn = await asyncpg.connect('postgresql://postgres@localhost/test')

asyncio.get_event_loop().run_until_complete(main())