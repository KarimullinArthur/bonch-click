import asyncio

from common import database


async def main():
    await database.init_models()
    await database.create_account("hello@mail.com", "secret")
    import time

    time.sleep(10)
    acc = await database.get_account("hello@mail.com")
    print(acc)


asyncio.run(main())
