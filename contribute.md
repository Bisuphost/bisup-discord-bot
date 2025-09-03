# Contributing to Bisup Discord Bot

Thanks for your interest in contributing! 🎉
This document explains how you can help improve the bot and the project structure.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Adding a New Command](#adding-a-new-command)
4. [Testing](#testing)
5. [Pull Request Guidelines](#pull-request-guidelines)

---

## Project Structure

```
bisup-discord-bot/
│── bot.py               # Entry point (starts the bot)
│── config.py            # API keys & bot token (ignored by git)
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
│── CONTRIBUTING.md      # Contribution guidelines
│── LICENSE              # MIT license
│
├── cogs/                # Modular commands (each feature is a cog)
│   ├── whois_lookup.py  # WHOIS lookup
│   ├── dns_lookup.py    # DNS record lookup
│   ├── ip_lookup.py     # IP & geolocation lookup
│   └── traffic.py       # Website traffic stats
│
├── utils/               # Helper functions
│   ├── formatters.py    # Embed formatting helpers
│   ├── api_helpers.py   # API-related functions
│   └── cache.py         # Optional caching
│
└── tests/               # Unit tests for commands
    └── test_whois.py
```

---

## Getting Started

1. **Fork the repository** and clone your fork:

```bash
git clone https://github.com/your-username/bisup-discord-bot.git
cd bisup-discord-bot
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Add your bot token and API keys**:

```python
# config.py
DISCORD_TOKEN = "your_token_here"
IPINFO_TOKEN = "optional_token"
```

4. **Run the bot**:

```bash
python bot.py
```

---

## Adding a New Command

1. Create a new file in `cogs/`, e.g., `my_command.py`.
2. Structure it like this:

```python
import discord
from discord.ext import commands

class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mycmd")
    async def my_command(self, ctx):
        await ctx.send("Hello world!")

async def setup(bot):
    await bot.add_cog(MyCommand(bot))
```

3. Restart the bot. Your new command should now be active.

---

## Testing

* Use the `tests/` folder to add unit tests for your functions.
* Make sure new commands don’t break existing functionality.

---

## Pull Request Guidelines

1. Fork the repo and create a new branch:

```bash
git checkout -b feature/my-feature
```

2. Make your changes and commit:

```bash
git add .
git commit -m "Add feature X"
```

3. Push your branch and open a Pull Request to the main repository.
4. Include a description of your changes and which commands were added/modified.

---

Thanks for contributing! Your help makes the Bisup Discord Bot better for everyone. 🚀
