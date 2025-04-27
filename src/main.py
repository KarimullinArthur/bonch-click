import asyncio

from bonchapi import BonchAPI

import database

database.create_table()
database.crud.create_account("yyy", "xxx")
users = database.crud.get_all_accounts()
print(users)


async def main():
    api = BonchAPI()
    for user in users:
        print(user.email)
        print(user.password)
        try:
            await api.login(user.email, user.password)
            await api.click_start_lesson()
        except:
            pass
        await asyncio.sleep(0.5)


asyncio.run(main())
