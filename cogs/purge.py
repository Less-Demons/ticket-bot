import discord
from discord.ext import commands

class Moderation10(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def clear(self, ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Chat has been purged")

def setup(client):
  client.add_cog(Moderation10(client))