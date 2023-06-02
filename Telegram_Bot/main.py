#!/usr/bin/python3

import asyncio
from sys import argv
import telegram


async def main():
    bot = telegram.Bot(argv[1])
    async with bot:
        print(await bot.get_me())
    #    print((await bot.get_updates())[0])
        await bot.send_message(text='Hi Emy', chat_id=956127600)


if __name__ == '__main__':
    asyncio.run(main())