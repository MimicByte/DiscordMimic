# Contributing to DiscordMimic

Welcome! This guide will help you get started with contributing to DiscordMimic, whether you're new to Discord bots, Python, or open source in general.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Understanding the Codebase](#understanding-the-codebase)
- [Creating Your First Extension](#creating-your-first-extension)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Your Changes](#testing-your-changes)
- [Submitting Changes](#submitting-changes)
- [Learning Resources](#learning-resources)

## Getting Started

### Prerequisites

Before you begin, make sure you have:

1. **Python 3.12 or higher** installed
2. **Git** for version control
3. **A Discord account** and a test server
4. **A Discord bot token** (see [Creating a Bot](#creating-a-bot))

### Creating a Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section and click "Add Bot"
4. Under "Token", click "Copy" to copy your bot token
5. **Important**: Keep this token secret!
6. Enable the necessary "Privileged Gateway Intents" if your bot needs them:
   - Presence Intent
   - Server Members Intent
   - Message Content Intent

### Inviting Your Bot to a Server

1. In the Developer Portal, go to "OAuth2" → "URL Generator"
2. Select scopes: `bot` and `applications.commands`
3. Select bot permissions based on what you need
4. Copy the generated URL and open it in your browser
5. Select your test server and authorize the bot

## Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MimicByte/DiscordMimic.git
cd DiscordMimic
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Your Bot Token

```bash
# On Linux/Mac:
export DISCORD_TOKEN="your_token_here"

# On Windows:
set DISCORD_TOKEN=your_token_here

# Or create a .env file (not committed to git):
echo "DISCORD_TOKEN=your_token_here" > .env
```

### 5. Configure the Bot

Run the bot once to generate the data directory:

```bash
python main.py
```

The bot will create `discordmimic/data/config.toml`. You can edit this file to configure:
- Discord intents (required for many features)
- Bot activity/status
- Logging levels
- And more (see ARCHITECTURE.md)

**Important**: Set the intents value based on what your bot needs. For example:
```toml
[discord]
# 3276799 = all non-privileged intents
# 32767 = all privileged intents enabled
intents = 3276799
```

To calculate intents, use the [Discord Intents Calculator](https://discord-intents-calculator.vercel.app/).

### 6. Stop and Restart

Press Ctrl+C to stop the bot, then restart it to test your configuration.

## Understanding the Codebase

### Key Files

- **`main.py`**: Entry point - handles initialization and startup
- **`discordmimic/core.py`**: Main `DiscordMimic` class extending interactions.Client
- **`discordmimic/mimicextension.py`**: Base class for creating extensions
- **`discordmimic/defaults/config.toml`**: Default configuration template

### Data Directory

When running, the bot creates:
- `discordmimic/data/config.toml` - Your bot's configuration
- `discordmimic/data/extensions/` - Your custom extensions
- `discordmimic/data/storage/` - Persistent storage for extensions

### Architecture Overview

Read [ARCHITECTURE.md](ARCHITECTURE.md) for a detailed explanation of:
- Project structure
- Core components
- Extension system
- Configuration options
- Design patterns

## Creating Your First Extension

Extensions are the primary way to add functionality to DiscordMimic. Here's a complete example:

### Step 1: Create Extension Directory

```bash
mkdir -p discordmimic/data/extensions/hello_world
```

### Step 2: Create `__init__.py`

Create `discordmimic/data/extensions/hello_world/__init__.py`:

```python
from discordmimic import MimicExtension
from interactions import slash_command, SlashContext

class HelloWorldExtension(MimicExtension):
    """A simple example extension"""
    
    async def setup(self):
        """Called when the bot is ready"""
        print("Hello World extension is ready!")
    
    @slash_command(
        name="hello",
        description="Say hello to the bot"
    )
    async def hello_command(self, ctx: SlashContext):
        """Simple hello command"""
        await ctx.send(f"Hello, {ctx.author.mention}! 👋")
    
    @slash_command(
        name="ping",
        description="Check if the bot is responsive"
    )
    async def ping_command(self, ctx: SlashContext):
        """Check bot latency"""
        latency = self.bot.latency
        await ctx.send(f"Pong! Latency: {latency:.2f}ms")

def setup(bot):
    """Entry point for the extension"""
    HelloWorldExtension(bot)
```

### Step 3: Enable the Extension

Edit `discordmimic/data/config.toml`:

```toml
[extensions]
enabled = ["hello_world"]
```

### Step 4: Test It

```bash
python main.py
```

In Discord, use `/hello` or `/ping` to test your commands!

## Code Style Guidelines

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use descriptive variable names
- Add docstrings to classes and functions
- Keep functions focused and small

### Extension Best Practices

1. **Inherit from MimicExtension**: Always use the base class
   ```python
   class MyExtension(MimicExtension):
       pass
   ```

2. **Override setup()**: Use for initialization
   ```python
   async def setup(self):
       # Your initialization code
       pass
   ```

3. **Use type hints**: Makes code more readable
   ```python
   async def my_command(self, ctx: SlashContext) -> None:
       pass
   ```

4. **Handle errors gracefully**: Catch exceptions and provide feedback
   ```python
   @slash_command(name="risky")
   async def risky_command(self, ctx: SlashContext):
       try:
           # Risky operation
           pass
       except Exception as e:
           await ctx.send(f"Error: {e}")
   ```

5. **Access bot resources**: Use self.bot for bot instance
   ```python
   config = self.bot.config
   storage_path = self.bot.storage
   ```

### Git Commit Messages

- Use present tense: "Add feature" not "Added feature"
- Be descriptive but concise
- Reference issues when applicable: "Fix #123: Resolve extension loading bug"

## Testing Your Changes

### Manual Testing

1. **Test in a development server**: Never test directly in production
2. **Test slash commands**: Use `/` to see if commands register
3. **Check console output**: Look for errors or warnings
4. **Test edge cases**: Try invalid inputs, missing permissions, etc.

### Testing Extensions

Create a test extension to validate your changes:

```python
from discordmimic import MimicExtension

class TestExtension(MimicExtension):
    async def setup(self):
        # Test that you can access bot resources
        assert self.bot.config is not None
        assert self.bot.storage is not None
        print("✓ All tests passed")

def setup(bot):
    TestExtension(bot)
```

### Common Issues

**Commands don't appear**:
- Wait 1-2 minutes for Discord to sync
- Check that `sync_interactions = true` in config
- Verify bot has `applications.commands` scope

**Bot doesn't start**:
- Check token is set correctly
- Verify intents are configured
- Look at console errors

**Extension doesn't load**:
- Check extension is in `enabled` list
- Verify `__init__.py` has `setup(bot)` function
- Look for Python syntax errors

## Submitting Changes

### Before Submitting

1. **Test thoroughly**: Ensure your changes work
2. **Update documentation**: If you change functionality
3. **Follow code style**: Keep consistency with existing code
4. **Small commits**: Make focused, atomic changes

### Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Commit: `git commit -m "Add my feature"`
5. Push: `git push origin feature/my-feature`
6. Open a Pull Request on GitHub
7. Describe your changes clearly
8. Wait for review and address feedback

## Learning Resources

### Essential Reading

1. **[ARCHITECTURE.md](ARCHITECTURE.md)**: Understand the codebase structure
2. **[interactions.py docs](https://interactions-py.github.io/interactions.py/)**: Learn the Discord library
3. **[Discord Developer Docs](https://discord.com/developers/docs)**: Discord API reference

### Learning Discord Bots

- **[Discord.py guide](https://discordpy.readthedocs.io/)**: Conceptually similar library
- **[interactions.py examples](https://github.com/interactions-py/interactions.py/tree/stable/examples)**: Official examples
- **[Discord API server](https://discord.gg/discord-api)**: Get help from the community

### Learning Python

- **[Python Tutorial](https://docs.python.org/3/tutorial/)**: Official Python guide
- **[Real Python](https://realpython.com/)**: Practical Python tutorials
- **[Async/await in Python](https://realpython.com/async-io-python/)**: Understanding async programming

### Useful Tools

- **[Discord Intents Calculator](https://discord-intents-calculator.vercel.app/)**: Calculate intent values
- **[Discord Permissions Calculator](https://discordapi.com/permissions.html)**: Calculate permission values
- **[Python Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)**: Type annotation reference

## Need Help?

- **Check existing issues**: Someone might have had the same problem
- **Read the documentation**: ARCHITECTURE.md covers most concepts
- **Ask questions**: Open an issue with the "question" label
- **Join Discord communities**: Discord API and interactions.py servers

## Next Steps

Now that you understand the basics:

1. ✅ Set up your development environment
2. ✅ Create a simple extension
3. 📚 Read ARCHITECTURE.md for deeper understanding
4. 🔨 Try creating a more complex extension with:
   - Event listeners (on_message_create, etc.)
   - Buttons and modals
   - Persistent storage
   - API interactions
5. 🚀 Share your extension or contribute to the core!

Happy coding! 🎉
