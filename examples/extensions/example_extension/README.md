# Example Extension

This is a comprehensive example extension that demonstrates common patterns and best practices for building DiscordMimic extensions.

## Features Demonstrated

### Slash Commands
- **Basic commands**: Simple command structure
- **Commands with options**: Required and optional parameters
- **Different option types**: String, Boolean, etc.
- **Error handling**: Graceful handling of exceptions

### Event Listeners
- **Message events**: Responding to messages (requires MESSAGE_CONTENT intent)
- **Bot mentions**: Detecting when the bot is mentioned

### Storage
- **Persistent data**: Reading and writing data to disk
- **JSON storage**: Using JSON for structured data

### Bot Integration
- **Accessing bot properties**: User info, guild count, latency
- **Using configuration**: Reading bot configuration
- **Storage directory**: Using the bot's storage path

## Commands

All commands are prefixed with `example_` to avoid conflicts:

- `/example_hello` - Simple greeting command
- `/example_info` - Display bot information
- `/example_counter` - Persistent counter (increments each time)
- `/example_echo <message> [loud]` - Echo back a message with optional uppercase
- `/example_choose <options>` - Randomly choose from comma-separated options
- `/example_error` - Demonstrate error handling

## Installation

### Option 1: Copy to Your Bot

1. Copy this entire directory to your bot's extensions folder:
   ```bash
   cp -r examples/extensions/example_extension discordmimic/data/extensions/
   ```

2. Enable it in `discordmimic/data/config.toml`:
   ```toml
   [extensions]
   enabled = ["example_extension"]
   ```

3. Restart the bot

### Option 2: Use as a Template

1. Copy this directory and rename it:
   ```bash
   cp -r examples/extensions/example_extension discordmimic/data/extensions/my_extension
   ```

2. Edit `__init__.py` to customize the extension:
   - Change the class name
   - Rename commands (remove `example_` prefix)
   - Add your own functionality

3. Enable your new extension in config

## Configuration Requirements

### Discord Intents

Some features require specific Discord intents:

- **Message Content Intent** (value: 32768): Required for `on_message_create` to read message content
- Without this intent, the message content event listener won't work properly

To enable in config:
```toml
[discord]
intents = 3276799  # Includes MESSAGE_CONTENT and other common intents
```

### Bot Permissions

Commands that interact with messages need:
- Read Messages
- Send Messages
- Read Message History

## Code Structure

```python
class ExampleExtension(MimicExtension):
    """Your extension class"""
    
    def __init__(self, bot):
        """Extension initialization"""
        super().__init__(bot)
        # Initialize variables
    
    async def setup(self):
        """Called when bot is ready"""
        # Perform setup that needs a ready bot
    
    @slash_command(...)
    async def my_command(self, ctx):
        """Your slash commands"""
        pass
    
    @listen()
    async def on_event(self, event):
        """Your event listeners"""
        pass
    
    def _helper_method(self):
        """Private helper methods"""
        pass

def setup(bot):
    """Required entry point"""
    ExampleExtension(bot)
```

## Learning Resources

After exploring this example, check out:

1. **[interactions.py Documentation](https://interactions-py.github.io/interactions.py/)** - Learn about all available features
2. **[Discord Developer Docs](https://discord.com/developers/docs)** - Understand Discord API concepts
3. **[ARCHITECTURE.md](../../../ARCHITECTURE.md)** - Deep dive into DiscordMimic architecture
4. **[CONTRIBUTING.md](../../../CONTRIBUTING.md)** - Complete guide for creating extensions

## Common Patterns

### Accessing Bot Resources

```python
# Bot configuration
config = self.bot.config
my_setting = config.get("my_section", {})

# Storage directory
storage_path = self.bot.storage
my_file = os.path.join(storage_path, "my_data.json")

# Bot properties
bot_user = self.bot.user
guilds = self.bot.guilds
latency = self.bot.latency
```

### Persistent Storage

```python
import json
import os

# Save data
def save_data(self, data):
    file_path = os.path.join(self.bot.storage, "my_data.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)

# Load data
def load_data(self):
    file_path = os.path.join(self.bot.storage, "my_data.json")
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Default value
```

### Error Handling

```python
@slash_command(name="safe_command")
async def safe_command(self, ctx: SlashContext):
    try:
        # Your code that might fail
        result = some_risky_operation()
        await ctx.send(f"Success: {result}")
    except SpecificError as e:
        # Handle specific errors
        await ctx.send(f"Known error: {e}")
    except Exception as e:
        # Catch-all for unexpected errors
        await ctx.send(f"Unexpected error: {e}")
        # Optionally log the error
        print(f"Error in safe_command: {e}")
```

### Deferred Responses

For long-running operations:

```python
@slash_command(name="slow_command")
async def slow_command(self, ctx: SlashContext):
    # Tell Discord we're working on it
    await ctx.defer()
    
    # Do slow operation
    result = await slow_async_operation()
    
    # Send the response
    await ctx.send(f"Done! Result: {result}")
```

## Tips for Extension Development

1. **Test thoroughly**: Use a test server to avoid issues in production
2. **Handle errors**: Always expect the unexpected and handle it gracefully
3. **Use type hints**: Makes code more maintainable and catches errors early
4. **Log important events**: Use print() or logging for debugging
5. **Document your code**: Write docstrings for classes and methods
6. **Follow naming conventions**: Use descriptive names for commands and variables
7. **Check permissions**: Ensure the bot has necessary permissions before operations
8. **Respect rate limits**: Be mindful of Discord's API rate limits

## Next Steps

Now that you've explored this example:

1. ✅ Understand the basic structure
2. ✅ See how commands work
3. 🔨 Try modifying the example
4. 🚀 Create your own extension from scratch
5. 📚 Explore more advanced interactions.py features:
   - Buttons and select menus
   - Modals (forms)
   - Context menus
   - Message components
   - Embeds

Happy coding! 🎉
