# DiscordMimic Architecture

## Overview

DiscordMimic is a Discord bot framework built on top of [interactions.py](https://github.com/interactions-py/interactions.py), designed to provide a flexible and extensible architecture for creating Discord bots with a focus on modularity through extensions.

## Project Structure

```
DiscordMimic/
├── main.py                          # Application entry point
├── discordmimic/                    # Core package
│   ├── __init__.py                  # Package exports
│   ├── core.py                      # Main bot class (DiscordMimic)
│   ├── mimicextension.py            # Base extension class
│   └── defaults/                    # Default configuration
│       └── config.toml              # Default configuration template
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Container configuration
├── compose.yaml                     # Docker Compose setup
└── README.md                        # Basic setup instructions
```

### Runtime Data Directory

When the bot runs, it creates a `discordmimic/data/` directory:
```
discordmimic/data/
├── config.toml                      # User configuration (copied from defaults)
├── extensions/                      # User-created extensions
│   └── <extension_name>/
│       ├── __init__.py              # Extension entry point
│       └── requirements.txt         # Extension-specific dependencies (optional)
└── storage/                         # General storage for extensions
```

## Core Components

### 1. main.py - Application Bootstrap

The entry point that:
- Creates necessary data directories
- Copies default configuration if not present
- Loads configuration from TOML file
- Installs extension-specific dependencies
- Initializes and starts the bot

**Key Functions:**
```python
def main():
    # Setup data directories
    # Load configuration
    # Install extension dependencies
    # Create bot instance
    # Start bot with Discord token
```

### 2. DiscordMimic (core.py) - Main Bot Class

Extends `interactions.Client` to provide:
- Configuration-based initialization
- Built-in logging setup
- Extension loading on ready
- Access to shared resources (config, storage)

**Key Features:**
- Configurable Discord client options via TOML
- Support for intents, activity, proxy settings, etc.
- Automatic extension loading from config
- Storage directory for persistence

**Attributes:**
- `config`: Loaded TOML configuration
- `database`: Placeholder for database connection (currently None)
- `extensions`: Placeholder for extension registry (currently None)
- `storage`: Path to shared storage directory

### 3. MimicExtension (mimicextension.py) - Base Extension Class

A specialized `Extension` class that provides:
- Deferred initialization (waits for bot to be ready)
- Automatic setup handling
- Clean extension lifecycle management

**Lifecycle:**
1. Extension is instantiated
2. Waits for bot to be ready
3. Calls `setup()` method (override this in your extension)
4. Marks as initialized

## Configuration System

Configuration is managed through TOML files located at `discordmimic/data/config.toml`.

### Configuration Sections

#### [discord]
Discord client configuration:
```toml
[discord]
intents = 0                          # Required: Discord intents bitmask
activity = "Playing a game"          # Optional: Bot status
auto_defer = true                    # Optional: Auto-defer interactions
delete_unused_application_cmds = false
disable_dm_commands = false
enforce_interaction_perms = true
fetch_members = false
logging_level = 20                   # INFO level
send_command_tracebacks = true
send_not_ready_messages = false
show_ratelimit_tracebacks = false
sync_ext = true
sync_interactions = true
proxy_url = "http://proxy:port"      # Optional: Proxy URL
proxy_auth = ["user", "pass"]        # Optional: Proxy authentication
```

#### [database]
Database connection settings (for future use):
```toml
[database]
user = ""
password = ""
host = ""
port = ""
```

#### [extensions]
Extension management:
```toml
[extensions]
enabled = ["example_extension", "another_extension"]
```

## Extension System

### Creating an Extension

1. Create a directory in `discordmimic/data/extensions/`:
   ```
   discordmimic/data/extensions/my_extension/
   ```

2. Create `__init__.py`:
   ```python
   from discordmimic import MimicExtension
   from interactions import slash_command
   
   class MyExtension(MimicExtension):
       async def setup(self):
           # Called when bot is ready
           print("My extension is setting up!")
       
       @slash_command(name="hello", description="Say hello")
       async def hello(self, ctx):
           await ctx.send("Hello from my extension!")
   
   def setup(bot):
       MyExtension(bot)
   ```

3. (Optional) Add `requirements.txt` for extension-specific dependencies:
   ```
   requests==2.31.0
   ```

4. Enable in `config.toml`:
   ```toml
   [extensions]
   enabled = ["my_extension"]
   ```

### Extension Loading Process

1. Bot starts and waits for `on_ready` event
2. Reads `enabled` list from config
3. Loads each extension using `bot.load_extension()`
4. Extensions are loaded from `discordmimic.data.extensions.<name>`
5. Each extension's `setup()` function is called
6. MimicExtension instances wait for bot to be ready before initializing

## Authentication & Security

### Discord Token

The bot requires a Discord bot token provided via environment variable:
```bash
export DISCORD_TOKEN="your_token_here"
```

This token is read by `main.py` and passed to `bot.start()`.

### Best Practices

- Never commit tokens to version control
- Use environment variables or secure secret management
- The `discordmimic/data/` directory is gitignored to prevent accidental commits

## Deployment

### Local Development

```bash
# Set token
export DISCORD_TOKEN="your_token_here"

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

### Docker

```bash
# Build and run with docker-compose
docker-compose up --build
```

Environment variables can be set in compose.yaml or via `.env` file.

## Dependencies

### Core Dependencies
- **interactions.py[voice]**: Discord API library with voice support
- **aiohttp**: Async HTTP client (used by interactions.py)

### System Requirements
- Python 3.12+ (uses `tomllib` from stdlib)
- Git (for Docker builds)
- FFmpeg (for voice functionality)
- libffi-dev, libnacl-dev (for voice encryption)

## Design Patterns

### 1. Configuration-Driven Design
All bot behavior is configurable through TOML files, making it easy to adjust without code changes.

### 2. Extension-Based Architecture
Core bot is minimal; functionality is added through extensions, promoting:
- Modularity
- Separation of concerns
- Easy feature addition/removal

### 3. Lazy Initialization
Extensions use deferred setup to ensure the bot is fully ready before initialization, avoiding race conditions.

### 4. Convention Over Configuration
- Extensions follow naming conventions
- Default values reduce configuration burden
- Sensible defaults for Discord client options

## Future Considerations

Based on the current architecture, potential areas for expansion:

1. **Database Integration**: The `database` config section and `self.database` attribute suggest planned database support
2. **Extension Registry**: The `self.extensions` attribute could track loaded extensions
3. **Storage Management**: Formalized storage API for extensions
4. **Hot Reload**: Dynamic extension loading/unloading
5. **Extension Dependencies**: Extensions depending on other extensions

## Common Patterns for Developers

### Accessing Bot Configuration
```python
class MyExtension(MimicExtension):
    async def setup(self):
        bot_config = self.bot.config
        my_setting = bot_config.get("my_section", {}).get("my_key", "default")
```

### Using Shared Storage
```python
class MyExtension(MimicExtension):
    async def setup(self):
        storage_path = self.bot.storage
        my_data_file = os.path.join(storage_path, "my_extension_data.json")
```

### Listening to Events
```python
from interactions import listen

class MyExtension(MimicExtension):
    @listen()
    async def on_message_create(self, event):
        # Handle message events
        pass
```

## Debugging Tips

1. **Enable Debug Logging**: Set `logging_level = 10` in config
2. **Check Extension Loading**: Watch console output for "extension loaded" messages
3. **Verify Configuration**: Ensure `config.toml` is in `discordmimic/data/`
4. **Check Intents**: Many features require specific Discord intents
5. **Extension Dependencies**: Check logs for pip install output

## Resources

- [interactions.py Documentation](https://interactions-py.github.io/interactions.py/)
- [Discord Developer Portal](https://discord.com/developers/docs)
- [Discord Intents Guide](https://discord.com/developers/docs/topics/gateway#gateway-intents)
