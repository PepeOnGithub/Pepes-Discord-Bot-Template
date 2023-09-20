import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# This is an example command 
@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description=f"Latency: {round(bot.latency * 1000)}ms",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)
  
# This is an example slash command
@bot.tree.command(name="ping", description="This is a bot tree interaction.")
async def ping_slash_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Pong",
        description=f"Latency: {round(bot.latency * 1000)}ms",
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)

# Replace 'BOT_TOKEN' with your actual bot token
bot.run('BOT_TOKEN')
