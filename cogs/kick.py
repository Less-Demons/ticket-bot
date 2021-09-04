import discord
from discord.ext import commands

class ModeraTion(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(embed=discord.Embed(
      title="Kicked",
      description=f"{member.mention} been Kicked.",
      color=0xFF5733))
    await member.send(embed=discord.Embed(
      title="Kicked",
      description=f"You have been kicked for {reason}.",
      color=0xFF5733))

def setup(client):
  client.add_cog(ModeraTion(client))