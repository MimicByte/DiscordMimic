# DiscordMimic

A flexible, extensible Discord bot framework built on [interactions.py](https://github.com/interactions-py/interactions.py). DiscordMimic provides a solid foundation for creating Discord bots with a modular extension system that makes it easy to add and manage features.

## ✨ Features

- 🧩 **Modular Extension System**: Add features through self-contained extensions
- ⚙️ **Configuration-Driven**: Customize bot behavior through simple TOML files
- 🔌 **Easy Setup**: Get started quickly with sensible defaults
- 🐳 **Docker Support**: Deploy easily with included Docker configuration
- 📦 **Dependency Management**: Extensions can specify their own dependencies
- 🎯 **Built on interactions.py**: Leverages a modern, well-maintained Discord library

## 🚀 Quick Start

> **New to Discord bots?** Check out [QUICKSTART.md](QUICKSTART.md) for a complete step-by-step guide!

### Prerequisites

- Python 3.12 or higher
- A Discord bot token ([Create one here](https://discord.com/developers/applications))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MimicByte/DiscordMimic.git
   cd DiscordMimic
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Discord token**
   ```bash
   export DISCORD_TOKEN="your_bot_token_here"
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

On first run, the bot will create a `discordmimic/data/` directory with a default configuration file.

### Configuration

Edit `discordmimic/data/config.toml` to configure your bot:

```toml
[discord]
intents = 3276799  # Discord intents (see documentation)
activity = "with extensions"

[extensions]
enabled = []  # List your extensions here
```

**Important**: You'll need to configure the `intents` value based on what features your bot needs. Use the [Discord Intents Calculator](https://discord-intents-calculator.vercel.app/) to determine the right value.

## 📚 Documentation

- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Complete guide for newcomers - learn how to create extensions and contribute
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Deep dive into the codebase structure and design patterns
- **[interactions.py docs](https://interactions-py.github.io/interactions.py/)**: Learn about the underlying Discord library

## 🧩 Creating Extensions

Extensions are the primary way to add functionality to DiscordMimic. Here's a simple example:

1. Create `discordmimic/data/extensions/my_extension/__init__.py`:

```python
from discordmimic import MimicExtension
from interactions import slash_command

class MyExtension(MimicExtension):
    @slash_command(name="hello", description="Say hello")
    async def hello(self, ctx):
        await ctx.send("Hello! 👋")

def setup(bot):
    MyExtension(bot)
```

2. Enable it in `config.toml`:

```toml
[extensions]
enabled = ["my_extension"]
```

3. Restart the bot and use `/hello` in Discord!

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md#creating-your-first-extension).

## 🐳 Docker Deployment

Run with Docker Compose:

```bash
docker-compose up --build
```

Make sure to set your `DISCORD_TOKEN` environment variable in `compose.yaml` or through a `.env` file.

## 🤝 Contributing

We welcome contributions! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

- **New to the project?** Start with [CONTRIBUTING.md](CONTRIBUTING.md)
- **Want to understand the code?** Read [ARCHITECTURE.md](ARCHITECTURE.md)
- **Found a bug?** Open an issue
- **Have a feature idea?** Open an issue to discuss it

## 📖 Learning Path

1. **Absolute Beginner?** Start with [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide
2. **Want to Contribute?** Read [CONTRIBUTING.md](CONTRIBUTING.md) for a complete newcomer guide
3. **Create Your First Extension**: Follow the tutorial in the contributing guide
4. **Explore the Architecture**: Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand the design
5. **Learn interactions.py**: Check out the [official documentation](https://interactions-py.github.io/interactions.py/)
6. **Build Something Cool**: Create your own extensions and share them!

## 📋 Requirements

- Python 3.12+
- interactions.py[voice] 5.14.0+
- aiohttp 3.9.5+

For voice functionality, additional system dependencies are required:
- FFmpeg
- libffi-dev
- libnacl-dev

See [Dockerfile](Dockerfile) for the complete list.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [interactions.py Documentation](https://interactions-py.github.io/interactions.py/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Discord API Documentation](https://discord.com/developers/docs)
- [Discord Intents Calculator](https://discord-intents-calculator.vercel.app/)

## ⚡ Environment Variables

- `DISCORD_TOKEN` (required): Your Discord bot token

---

**Ready to get started?** Head over to [CONTRIBUTING.md](CONTRIBUTING.md) for a complete guide!