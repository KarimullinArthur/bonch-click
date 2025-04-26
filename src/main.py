import asyncio

from bonchapi import BonchAPI

from config import config


users = [
        {
            "login": config.mail,
            "password": config.password
        },
        {
            "login": "secret",
            "password": "ha-ha, secret" 
        }
]

print(users)

async def main():
    api = BonchAPI()
    for user in users:
        print(user["login"])
        print(user["password"])
        try:
            await api.login(user["login"], user["password"])
            await api.click_start_lesson()
        except:
            pass
        await asyncio.sleep(0.5)


asyncio.run(main())
