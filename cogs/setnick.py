import discord
from discord.ext import commands

class mod(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_nicknames=True)
  async def setnick(self, ctx, member: discord.Member, *, nick=None):
    old_nick = member.display_name

    await member.edit(nick=nick)

    new_nick = member.display_name

    await ctx.send(f'Changed nick from *{old_nick}* to *{new_nick}*')

def setup(client):
  client.add_cog(mod(client))