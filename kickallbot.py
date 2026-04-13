



import discord
from discord.ext import commands

# --- CONFIGURATION ---
BOT_TOKEN = "your token here" # Replace with your bot token
COMMAND_PREFIX = "!"
# ---------------------

intents = discord.Intents.all() # Required to fetch all members

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Ready. Use !kickall in your server.")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kickall(ctx, *, reason: str = "Mass kick initiated by owner."):
    """Kicks all members except the server owner and the bot itself."""

    # Only the server owner can run this
    if ctx.author != ctx.guild.owner:
        await ctx.send("❌ Only the server owner can use this command.")
        return

    guild = ctx.guild
    owner = guild.owner
    kicked = 0
    skipped = 0
    failed = 0

    await ctx.send(f"⚠️ Starting kick of all members except the owner. Reason: `{reason}`")

    for member in guild.members:
        # Skip the owner and the bot itself
        if member == owner or member == bot.user:
            skipped += 1
            continue

        # Can't kick members with a higher or equal role than the bot
        if member.top_role >= ctx.guild.me.top_role:
            print(f"Skipped {member} — role too high.")
            skipped += 1
            continue

        try:
            await member.kick(reason=reason)
            print(f"Kicked: {member}")
            kicked += 1
        except discord.Forbidden:
            print(f"Failed (no permission): {member}")
            failed += 1
        except discord.HTTPException as e:
            print(f"Failed (HTTP error) for {member}: {e}")
            failed += 1

    await ctx.send(
        f"✅ Done!\n"
        f"👢 Kicked: **{kicked}**\n"
        f"⏭️ Skipped: **{skipped}**\n"
        f"❌ Failed: **{failed}**"
    )

bot.run(BOT_TOKEN)