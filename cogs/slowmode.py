import discord
from discord.ext import commands

class MoD(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def slowmode(self, ctx, sec: int = None, channel: discord.TextChannel = None):
    if not sec:
        sec = 0
    if not channel:
        channel = ctx.channel

    await channel.edit(slowmode_delay=sec)

    await channel.send(f'This channel is now on **{sec}s** slowmode')

def setup(client):
  client.add_cog(MoD(client))