# Module Imports
import os
import tomllib
import shutil
import subprocess
import sys
import glob

from discordmimic import DiscordMimic


def main():
    if not os.path.exists("discordmimic/data"):
        os.makedirs("discordmimic/data")

    if not os.path.exists("discordmimic/data/config.toml"):
        shutil.copy(
            "discordmimic/defaults/config.toml", "discordmimic/data/config.toml"
        )

    if not os.path.exists("discordmimic/data/extensions"):
        os.makedirs("discordmimic/data/extensions")

    with open("discordmimic/data/config.toml", "rb") as config_file:
        config = tomllib.load(config_file)

    print(os.listdir())
    print(os.listdir("discordmimic"))
    print(os.listdir("discordmimic/data"))
    print(os.listdir("discordmimic/data/extensions"))

    extension_requirements = glob.glob("discordmimic/data/extensions/**/*.txt")
    print("Files Found: ", extension_requirements)
    for requirement in extension_requirements:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", requirement]
        )

    bot = DiscordMimic(config)

    bot.start(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
