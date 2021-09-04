import discord
from discord.ext import commands

class Moderation2(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def mute(self, ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(embed=discord.Embed(
        title="Muted",
        description=f"{member.mention} been muted for {reason}.",
        color=0xFF5733))
    await member.send(embed=discord.Embed(
        title="Muted",
        description=f"You have been muted in the {guild.name} for {reason}.",
        color=0xFF5733))

def setup(client):
  client.add_cog(Moderation2(client))