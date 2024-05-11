# Module Imports
import os
import logging

from interactions import (
    Client,
    Intents,
)
from interactions.api.events import MessageCreate


def main():
    logging.basicConfig()
    cls_log = logging.getLogger(__name__)
    cls_log.setLevel(logging.DEBUG)

    bot = Client(
        intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
        sync_interactions=True,
        asyncio_debug=True,
        logger=cls_log,
        delete_unused_application_cmds=True,
    )

    @bot.listen()
    async def on_ready():
        print("Ready")
        print(f"This bot is owned by {bot.owner}")

    @bot.listen()
    async def on_message_create(event: MessageCreate):

        if bot.user.mention in event.message.content:
            await event.message.reply("Hello!")

    bot.start(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
