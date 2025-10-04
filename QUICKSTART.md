# DiscordMimic Quick Start Guide

Get your Discord bot running in 5 minutes! ⚡

## Prerequisites Checklist

- [ ] Python 3.12+ installed ([Download](https://www.python.org/downloads/))
- [ ] Git installed ([Download](https://git-scm.com/downloads))
- [ ] Discord account
- [ ] Discord bot token (see below if you don't have one)

## Step 1: Get a Discord Bot Token (5 minutes)

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** and give it a name (e.g., "My First Bot")
3. Click on **"Bot"** in the left sidebar
4. Click **"Reset Token"** (or "Add Bot" if this is your first time)
5. **Copy the token** and save it somewhere safe - you'll need it soon!
6. Scroll down and enable these if needed:
   - ☑️ Presence Intent
   - ☑️ Server Members Intent  
   - ☑️ Message Content Intent

## Step 2: Invite Your Bot to a Server (2 minutes)

1. In the Developer Portal, click **"OAuth2"** → **"URL Generator"**
2. Select these scopes:
   - ☑️ `bot`
   - ☑️ `applications.commands`
3. Select bot permissions (start with these):
   - ☑️ Send Messages
   - ☑️ Read Messages/View Channels
   - ☑️ Use Slash Commands
4. **Copy the generated URL** at the bottom
5. Open the URL in your browser
6. Select your test server and click **"Authorize"**

## Step 3: Install DiscordMimic (2 minutes)

Open your terminal/command prompt:

```bash
# Clone the repository
git clone https://github.com/MimicByte/DiscordMimic.git
cd DiscordMimic

# Install dependencies
pip install -r requirements.txt
```

## Step 4: Configure Your Bot (1 minute)

### Set your bot token:

**On Linux/Mac:**
```bash
export DISCORD_TOKEN="paste_your_token_here"
```

**On Windows (Command Prompt):**
```cmd
set DISCORD_TOKEN=paste_your_token_here
```

**On Windows (PowerShell):**
```powershell
$env:DISCORD_TOKEN="paste_your_token_here"
```

### Run the bot once to create config:
```bash
python main.py
```

Press `Ctrl+C` to stop it after you see "Ready".

### Edit the config file:

Open `discordmimic/data/config.toml` in a text editor and set intents:

```toml
[discord]
intents = 3276799
```

**What are intents?** Think of them as permissions for what your bot can see and do. The value `3276799` enables common features. [Learn more about intents](https://discord.com/developers/docs/topics/gateway#gateway-intents).

## Step 5: Start Your Bot! 🚀

```bash
python main.py
```

You should see:
```
Ready
This bot is owned by YourUsername#1234
```

**Congratulations!** Your bot is now online! 🎉

## Step 6: Try the Example Extension (Optional)

Want to add some commands? Let's install the example extension:

```bash
# Copy the example extension
cp -r examples/extensions/example_extension discordmimic/data/extensions/
```

Edit `discordmimic/data/config.toml`:
```toml
[extensions]
enabled = ["example_extension"]
```

Restart your bot:
```bash
python main.py
```

Now in Discord, type `/example_hello` and watch your bot respond! 🎮

### Available Example Commands:
- `/example_hello` - Get a greeting
- `/example_info` - See bot information
- `/example_counter` - Increment a counter
- `/example_echo <message>` - Echo back a message
- `/example_choose <options>` - Make a random choice

## What's Next?

### Learn to Create Your Own Extensions

Pick your learning style:

1. **Quick Tutorial**: [CONTRIBUTING.md - Creating Your First Extension](CONTRIBUTING.md#creating-your-first-extension)
2. **Example Code**: Study `examples/extensions/example_extension/__init__.py`
3. **Deep Dive**: Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand how everything works

### Create Your First Extension

Create a new file: `discordmimic/data/extensions/my_bot/__init__.py`

```python
from discordmimic import MimicExtension
from interactions import slash_command, SlashContext

class MyBot(MimicExtension):
    @slash_command(name="hello", description="My first command!")
    async def hello(self, ctx: SlashContext):
        await ctx.send("Hello! This is my first bot command! 🎉")

def setup(bot):
    MyBot(bot)
```

Enable it in `config.toml`:
```toml
[extensions]
enabled = ["my_bot"]
```

Restart and try `/hello`! 🚀

## Troubleshooting

### Bot doesn't come online
- ✅ Check your token is correct
- ✅ Check internet connection
- ✅ Look for error messages in the console

### Commands don't appear
- ✅ Wait 1-2 minutes for Discord to sync
- ✅ Check bot has `applications.commands` scope
- ✅ Try in a different channel
- ✅ Make sure bot is invited to the server

### "Missing Access" or "Missing Permissions"
- ✅ Check bot has required permissions
- ✅ Verify bot role is high enough in role hierarchy
- ✅ Check channel-specific permissions

### Intents Error
- ✅ Enable required intents in Developer Portal
- ✅ Set correct intents value in `config.toml`

### Extension doesn't load
- ✅ Check extension name in `enabled` list
- ✅ Verify `__init__.py` has `setup(bot)` function
- ✅ Look for Python syntax errors in console

## Common Questions

**Q: Is my token safe?**  
A: Never share your token or commit it to git! If exposed, reset it immediately in the Developer Portal.

**Q: Can I run multiple bots?**  
A: Yes! Just create different applications in the Developer Portal and use different tokens.

**Q: How do I stop the bot?**  
A: Press `Ctrl+C` in the terminal.

**Q: Where is my data stored?**  
A: Everything is in the `discordmimic/data/` directory (config, extensions, storage).

**Q: Can I deploy this to a server?**  
A: Yes! See [README.md](README.md) for Docker deployment instructions.

## Need More Help?

- 📖 **Full Documentation**: See [README.md](README.md)
- 🎓 **Complete Guide**: Read [CONTRIBUTING.md](CONTRIBUTING.md)
- 🏗️ **Architecture Details**: Check [ARCHITECTURE.md](ARCHITECTURE.md)
- 💬 **Ask Questions**: Open an issue on GitHub
- 📚 **Learn interactions.py**: [Official Docs](https://interactions-py.github.io/interactions.py/)

## Command Reference Card

```bash
# Start bot
python main.py

# Install new dependency
pip install package_name

# Check Python version
python --version

# Update dependencies
pip install -r requirements.txt --upgrade

# Check git status
git status

# View config
cat discordmimic/data/config.toml

# List extensions
ls discordmimic/data/extensions/
```

---

**Ready to build something awesome?** Start with [CONTRIBUTING.md](CONTRIBUTING.md)! 🚀
