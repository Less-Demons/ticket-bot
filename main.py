import nextcord, flask, discord, keep_alive, os, random, asyncio
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix ="'", help_command=None)

@client.event
async def on_ready():
    # Setting `Playing ` status
    await client.change_presence(activity=discord.Game(
        name=f"on {len(client.guilds)} servers"))

    # Setting `Listening ` status
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="To Commands"))

    # Setting `Watching ` status
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="/help"))
    print("client online")


async def ch_pr():
    await client.wait_until_ready()

    statuses = [
        "Join our support server https://discord.gg/qFeZnVza77",
        f"on {len(client.guilds)} servers | .help", "discord.py", "In Development", f"{round(client.latency * 1000)}ms"
    ]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(10)


client.loop.create_task(ch_pr())
client.run

@client.event
async def on_member_join(member):
  print("{member} has joined a server.")

@client.event
async def on_member_remove(member):
  print("{member} has left the server.")

@client.command()
async def load(ctx, extension):
  client.load_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
  client.load_extension(f"cogs.{extension}")
  client.unload_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid Command Used.')
  
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please pass in all required arguments.')

  if isinstance(error, commands.MissingPermissions):
    await ctx.send('You do not have the Required Permissions.')
  
@client.command()
@commands.has_permissions(administrator=True)
async def leave(message):
    await message.author.guild.leave()

@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
        
    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))
my_secret = os.environ['TOKEN']