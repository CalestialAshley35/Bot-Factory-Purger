import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    if amount <= 0:
        await ctx.send("Please specify a number greater than 0.")
        return

    if amount > 89:
        await ctx.send("You can only delete up to 89 messages at a time.")
        return

    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f'Successfully deleted {len(deleted)} messages.', delete_after=5)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please provide a valid number of messages to delete.")
    else:
        await ctx.send("An error occurred while trying to purge messages.")

# Replace 'your-bot-token' with your actual bot token
bot.run('your-bot-token')
