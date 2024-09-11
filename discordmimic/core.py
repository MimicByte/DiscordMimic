import logging

from interactions import (
    Client,
    Intents,
    listen,
    MISSING,
)


class DiscordMimic(Client):
    def __init__(self, config, *args, **kwargs):
        logging.basicConfig()
        cls_log = logging.getLogger(__name__)
        cls_log.setLevel(logging.DEBUG)

        intents = Intents.DEFAULT
        intents._value_ = config["discord"]["intents"]

        super().__init__(
            *args,
            activity=config["discord"].get("activity", None),
            asyncio_debug=True,
            auto_defer=config["discord"].get("auto_defer", MISSING),
            delete_unused_application_cmds=config["discord"].get(
                "delete_unused_application_cmds", False
            ),
            disable_dm_commands=config["discord"].get("disable_dm_commands", False),
            enforce_interaction_perms=config["discord"].get(
                "enforce_interaction_perms", True
            ),
            fetch_members=config["discord"].get("fetch_members", False),
            intents=intents,
            logger=cls_log,
            logging_level=config["discord"].get("logging_level", logging.INFO),
            send_command_tracebacks=config["discord"].get(
                "send_command_tracebacks", True
            ),
            send_not_ready_messages=config["discord"].get(
                "send_not_ready_messages", False
            ),
            show_ratelimit_tracebacks=config["discord"].get(
                "show_ratelimit_tracebacks", False
            ),
            sync_ext=config["discord"].get("sync_ext", True),
            sync_interactions=config["discord"].get("sync_interactions", True),
            proxy_url=config["discord"].get("proxy_url", None),
            proxy_auth=(
                tuple(config["discord"].get("proxy_auth"))
                if config["discord"].get("proxy_auth", None)
                else None
            ),
            **kwargs,
        )

        self.config = config
        self.database = None
        self.extensions = None
        self.storage = "discordmimic/data/storage/"

    @listen()
    async def on_ready(self):
        print("Ready")
        print(f"This bot is owned by {self.owner}")

        enabled_extensions = self.config["extensions"].get("enabled", [])
        for extension in enabled_extensions:
            self.load_extension("discordmimic.data.extensions." + extension)
