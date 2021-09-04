import discord
from discord.ext import commands

class Moderation(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(embed=discord.Embed(
      title="Banned",
      description=f"{member.mention} has been Banned.",
      color=0xFF5733))
    await member.send(embed=discord.Embed(
      title="Banned",
      description=f"You have been Banned for {reason}.",
      color=0xFF5733))

def setup(client):
  client.add_cog(Moderation(client))