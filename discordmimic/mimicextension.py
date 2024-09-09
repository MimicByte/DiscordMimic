import asyncio
from interactions import Extension, listen


class MimicExtension(Extension):
    def __init__(self, bot):
        self.initialized = False
        asyncio.create_task(self._setup())

    @listen()
    async def on_startup(self):
        if not self.initialized:
            await self._setup()

    async def _setup(self):
        if not self.bot.is_ready:
            return

        self.initialized = True
        print(f"{self.__class__.__name__} extension loaded")
        await self.setup()

    async def setup(self):
        pass
