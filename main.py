# Module Imports
import os
import logging
import tomllib
import shutil

from interactions import (
    Client,
    Intents,
)


def main():
    if not os.path.exists("DiscordMimic/data"):
        os.makedirs("DiscordMimic/data")

    if not os.path.exists("DiscordMimic/data/config.toml"):
        shutil.copy(
            "DiscordMimic/defaults/config.toml", "DiscordMimic/data/config.toml"
        )

    if not os.path.exists("DiscordMimic/data/modules"):
        os.makedirs("DiscordMimic/data/modules")

    with open("DiscordMimic/data/config.toml", "rb") as config_file:
        config = tomllib.load(config_file)

    logging.basicConfig()
    cls_log = logging.getLogger(__name__)
    cls_log.setLevel(logging.DEBUG)

    intents = Intents.DEFAULT
    intents._value_ = config["discord"]["intents"]

    bot = Client(
        intents=intents,
        sync_interactions=True,
        asyncio_debug=True,
        logger=cls_log,
        delete_unused_application_cmds=True,
    )

    @bot.listen()
    async def on_ready():
        print("Ready")
        print(f"This bot is owned by {bot.owner}")

    bot.start(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
