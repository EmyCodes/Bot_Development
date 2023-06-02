#!/usr/bin/python3

import asyncio
from sys import argv
import telegram


async def main():
    bot = telegram.Bot(argv[1])
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())