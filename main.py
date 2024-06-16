# Module Imports
import os
import tomllib
import shutil

from discordmimic import DiscordMimic


def main():
    if not os.path.exists("discordmimic/data"):
        os.makedirs("discordmimic/data")

    if not os.path.exists("discordmimic/data/config.toml"):
        shutil.copy(
            "discordmimic/defaults/config.toml", "discordmimic/data/config.toml"
        )

    if not os.path.exists("discordmimic/data/modules"):
        os.makedirs("discordmimic/data/modules")

    with open("discordmimic/data/config.toml", "rb") as config_file:
        config = tomllib.load(config_file)

    bot = DiscordMimic(config)

    bot.start(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
