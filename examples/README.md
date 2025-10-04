# DiscordMimic Examples

This directory contains example code to help you learn how to build extensions for DiscordMimic.

## Available Examples

### Example Extension

**Location**: `extensions/example_extension/`

A comprehensive example that demonstrates:
- Basic slash commands
- Commands with options
- Event listeners
- Persistent storage
- Error handling
- Accessing bot configuration

**Commands provided:**
- `/example_hello` - Simple greeting
- `/example_info` - Bot information
- `/example_counter` - Persistent counter
- `/example_echo` - Echo with options
- `/example_choose` - Random choice
- `/example_error` - Error handling demo

See [`extensions/example_extension/README.md`](extensions/example_extension/README.md) for detailed documentation.

## Using Examples

### Quick Test

To test an example extension:

1. Copy it to your bot's extensions directory:
   ```bash
   cp -r examples/extensions/example_extension discordmimic/data/extensions/
   ```

2. Enable it in your config (`discordmimic/data/config.toml`):
   ```toml
   [extensions]
   enabled = ["example_extension"]
   ```

3. Restart your bot and try the commands!

### Using as a Template

To create your own extension based on an example:

1. Copy and rename:
   ```bash
   cp -r examples/extensions/example_extension discordmimic/data/extensions/my_extension
   ```

2. Edit `discordmimic/data/extensions/my_extension/__init__.py`:
   - Change the class name
   - Rename/modify commands
   - Add your functionality

3. Enable your extension in config

4. Restart and test!

## Learning Path

If you're new to DiscordMimic, follow this path:

1. **Read the Docs**
   - Start with [CONTRIBUTING.md](../CONTRIBUTING.md) for a complete newcomer guide
   - Then read [ARCHITECTURE.md](../ARCHITECTURE.md) to understand the structure

2. **Explore the Example**
   - Read through `example_extension/__init__.py`
   - See the different patterns and techniques used
   - Try running it and using the commands

3. **Experiment**
   - Modify the example to add your own commands
   - Try different command options and event listeners
   - Break things and learn from errors!

4. **Build Your Own**
   - Start with a simple extension
   - Add features incrementally
   - Test thoroughly

5. **Go Deeper**
   - Explore [interactions.py docs](https://interactions-py.github.io/interactions.py/)
   - Try advanced features (buttons, modals, etc.)
   - Build something awesome!

## Need More Examples?

If you'd like to see examples of specific features, consider:

1. **interactions.py Examples**: The underlying library has extensive examples
   - [Official Examples](https://github.com/interactions-py/interactions.py/tree/stable/examples)
   
2. **Discord.py Guide**: Conceptually similar (though different library)
   - [Discord.py Examples](https://github.com/Rapptz/discord.py/tree/master/examples)

3. **Request an Example**: Open an issue requesting a specific example

## Contributing Examples

Have a cool extension that others might learn from? Consider contributing it!

1. Create your example extension in `examples/extensions/your_example/`
2. Add a README.md explaining what it demonstrates
3. Make sure it's well-commented and follows best practices
4. Submit a pull request

## Tips for Learning

- **Start Simple**: Begin with basic commands, add complexity gradually
- **Read Error Messages**: They usually tell you exactly what's wrong
- **Use Print Statements**: Debug by printing values
- **Test in a Safe Server**: Never test directly in production
- **Ask Questions**: Open issues if you're stuck
- **Read Others' Code**: Learn from existing extensions

## Additional Resources

- [CONTRIBUTING.md](../CONTRIBUTING.md) - Complete newcomer guide
- [ARCHITECTURE.md](../ARCHITECTURE.md) - Codebase structure
- [interactions.py Docs](https://interactions-py.github.io/interactions.py/) - Library reference
- [Discord Developer Docs](https://discord.com/developers/docs) - API documentation

Happy learning! 🚀
