import discord, json, asyncio
from discord.ext import commands

class Ticket4(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def close(self, ctx):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower(
            ) == "close"

        try:

            em = discord.Embed(
                title="Hercules Tickets",
                description=
                "Are you sure you want to close this ticket? Reply with `close` if you are sure.",
                color=0x00a8ff)

            await ctx.send(embed=em)
            await ctx.channel.delete()

            index = data["ticket-channel-ids"].index(channel_id)
            del data["ticket-channel-ids"][index]

            with open('data.json', 'w') as f:
                json.dump(data, f)

        except asyncio.TimeoutError:
            em = discord.Embed(
                title="Auroris Tickets",
                description=
                "You have run out of time to close this ticket. Please run the command again.",
                color=0x00a8ff)
            await ctx.send(embed=em)

def setup(client):
  client.add_cog(Ticket4(client))