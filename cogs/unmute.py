import discord
from discord.ext import commands

class MOD(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def unmute(self, ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(
        embed=discord.Embed(title="UnMuted",
                            description=f"{member.mention} been unmuted.",
                            color=0xFF5733))
    await member.send(embed=discord.Embed(
        title="UnMuted",
        description=f"You have been unmuted in {ctx.author.guild.name}.",
        color=0xFF5733))

def setup(client):
  client.add_cog(MOD(client))