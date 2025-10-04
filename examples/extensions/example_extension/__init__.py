"""
Example Extension for DiscordMimic

This extension demonstrates common patterns and best practices for building
DiscordMimic extensions. Use this as a template for your own extensions!

Features demonstrated:
- Slash commands with options
- Event listeners
- Using bot configuration
- Persistent storage
- Error handling
"""

import os
import json
from interactions import (
    slash_command,
    slash_option,
    SlashContext,
    OptionType,
    listen,
    Message,
)
from discordmimic import MimicExtension


class ExampleExtension(MimicExtension):
    """
    Example extension showcasing common functionality.
    
    This extension provides several example commands and demonstrates
    how to interact with the bot's features.
    """
    
    def __init__(self, bot):
        """Initialize the extension."""
        super().__init__(bot)
        self.counter_file = None
    
    async def setup(self):
        """
        Called when the bot is ready.
        
        This is where you should do any initialization that requires
        the bot to be fully loaded (e.g., accessing guilds, channels).
        """
        print("Example extension is setting up...")
        
        # Set up persistent storage for this extension
        self.counter_file = os.path.join(
            self.bot.storage,
            "example_counter.json"
        )
        
        # Load or initialize counter data
        if not os.path.exists(self.counter_file):
            self._save_counter(0)
        
        print("Example extension ready!")
    
    # =========================================================================
    # Slash Commands
    # =========================================================================
    
    @slash_command(
        name="example_hello",
        description="A simple hello command"
    )
    async def hello_command(self, ctx: SlashContext):
        """
        Simple command that greets the user.
        
        This demonstrates the most basic slash command.
        """
        await ctx.send(f"Hello, {ctx.author.mention}! 👋")
    
    @slash_command(
        name="example_info",
        description="Get information about this bot"
    )
    async def info_command(self, ctx: SlashContext):
        """
        Display information about the bot.
        
        This shows how to access bot properties and configuration.
        """
        bot_user = self.bot.user
        guild_count = len(self.bot.guilds)
        
        info_message = (
            f"**Bot Information**\n"
            f"Name: {bot_user.username}\n"
            f"ID: {bot_user.id}\n"
            f"Servers: {guild_count}\n"
            f"Latency: {self.bot.latency:.2f}ms"
        )
        
        await ctx.send(info_message)
    
    @slash_command(
        name="example_counter",
        description="Increment and display a counter"
    )
    async def counter_command(self, ctx: SlashContext):
        """
        Demonstrate persistent storage.
        
        This command increments a counter stored on disk and displays it.
        Shows how to persist data between bot restarts.
        """
        # Load current value
        count = self._load_counter()
        
        # Increment
        count += 1
        
        # Save new value
        self._save_counter(count)
        
        await ctx.send(f"Counter: {count} 🔢")
    
    @slash_command(
        name="example_echo",
        description="Echo back a message"
    )
    @slash_option(
        name="message",
        description="The message to echo",
        required=True,
        opt_type=OptionType.STRING
    )
    @slash_option(
        name="loud",
        description="Make the message uppercase",
        required=False,
        opt_type=OptionType.BOOLEAN
    )
    async def echo_command(self, ctx: SlashContext, message: str, loud: bool = False):
        """
        Echo a message with optional formatting.
        
        This demonstrates:
        - Required and optional command options
        - Different option types
        - Processing user input
        """
        response = message.upper() if loud else message
        await ctx.send(f"Echo: {response}")
    
    @slash_command(
        name="example_choose",
        description="Choose between options"
    )
    @slash_option(
        name="options",
        description="Comma-separated options to choose from",
        required=True,
        opt_type=OptionType.STRING
    )
    async def choose_command(self, ctx: SlashContext, options: str):
        """
        Randomly choose from provided options.
        
        This demonstrates string processing and randomization.
        """
        import random
        
        # Split and clean options
        choices = [opt.strip() for opt in options.split(",") if opt.strip()]
        
        if not choices:
            await ctx.send("Please provide at least one option!")
            return
        
        if len(choices) == 1:
            await ctx.send(f"There's only one option: **{choices[0]}**")
            return
        
        choice = random.choice(choices)
        await ctx.send(f"I choose: **{choice}** 🎲")
    
    @slash_command(
        name="example_error",
        description="Demonstrate error handling"
    )
    async def error_command(self, ctx: SlashContext):
        """
        Show how to handle errors gracefully.
        
        This command intentionally demonstrates error handling.
        """
        try:
            # This will raise an error
            result = 1 / 0
        except ZeroDivisionError:
            await ctx.send(
                "⚠️ Oops! I caught a division by zero error. "
                "This demonstrates graceful error handling."
            )
        except Exception as e:
            # Always good to have a general catch-all
            await ctx.send(f"An unexpected error occurred: {e}")
    
    # =========================================================================
    # Event Listeners
    # =========================================================================
    
    @listen()
    async def on_message_create(self, event):
        """
        Listen for messages (requires MESSAGE_CONTENT intent).
        
        This demonstrates:
        - Event listeners
        - Filtering messages
        - Responding to non-command messages
        
        Note: This requires the MESSAGE_CONTENT intent to be enabled.
        """
        message: Message = event.message
        
        # Ignore messages from bots (including ourselves)
        if message.author.bot:
            return
        
        # Example: Respond to mentions
        if self.bot.user.mentioned_in(message):
            await message.reply(
                "You mentioned me! Try using my slash commands with `/example_`"
            )
    
    # =========================================================================
    # Helper Methods
    # =========================================================================
    
    def _load_counter(self) -> int:
        """Load counter value from persistent storage."""
        try:
            with open(self.counter_file, 'r') as f:
                data = json.load(f)
                return data.get('count', 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
    
    def _save_counter(self, count: int) -> None:
        """Save counter value to persistent storage."""
        with open(self.counter_file, 'w') as f:
            json.dump({'count': count}, f)


def setup(bot):
    """
    Required entry point for the extension.
    
    This function is called by the bot when loading the extension.
    It should instantiate your extension class.
    """
    ExampleExtension(bot)
