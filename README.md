# 👢 kick bbot

A simple Discord bot that kicks all members from a server except the owner.

## Features

- Kicks every member in the server with a single command
- Automatically skips the server owner and the bot itself
- Skips members with roles higher than the bot (Discord limitation)
- Reports how many members were kicked, skipped, or failed

## Requirements

- Python 3.11+
- `discord.py`

## Setup

### 1. Install dependencies

```bash
pip install discord.py
```

### 2. Create a Discord bot

1. Go to https://discord.com/developers/applications
2. Click **New Application** and name it
3. Go to the **Bot** tab and click **Reset Token** — copy your token
4. Under **Privileged Gateway Intents**, enable:
   - **Server Members Intent**
   - **Message Content Intent**
5. Click **Save Changes**

### 3. Configure the bot

Open `kickallbot.py` and replace the placeholder with your token:

```python
BOT_TOKEN = "your_token_here"
```

> ⚠️ Never share or commit your real token to GitHub.

### 4. Invite the bot to your server

1. Go to **OAuth2 → URL Generator**
2. Select scope: `bot`
3. Select permission: `Kick Members`
4. Copy the generated URL and open it in your browser to invite the bot

### 5. Set up roles

In your Discord server, go to **Server Settings → Roles** and drag the bot's role **above** the roles of members you want to kick. The bot cannot kick anyone with a higher role than itself.

### 6. Run the bot

```bash
python kickallbot.py
```

## Usage

In any channel in your server, type:

```
!kickall
```

Only the **server owner** can use this command. The bot will kick all members except the owner and itself, then send a summary.

## Notes

- This is a personal/experimental bot — use responsibly
- The bot cannot kick members whose role is equal to or higher than the bot's role
- Revoking or resetting the token immediately invalidates it — do this if it's ever exposed

## License

MIT
