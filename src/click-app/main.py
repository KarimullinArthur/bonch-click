#!/usr/bin/env python3
import asyncio

from bonchapi import BonchAPI
from loguru import logger

from common import database

logger.add("logs/info.log", format="{time} {level} {message}", level="INFO")
users = database.crud.get_all_accounts()
print(users)


async def main():
    api = BonchAPI()
    for user in users:
        try:
            await api.login(user.email, user.password)
            await api.click_start_lesson()
            logger.info(f"Clicked for {user.email}")
        except:
            pass
        await asyncio.sleep(0.5)
    logger.info("All has been Clicked!")


asyncio.run(main())
