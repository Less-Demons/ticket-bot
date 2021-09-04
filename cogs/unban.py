import discord
from discord.ext import commands

class Development(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if (user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(description="{user.mention} was unbanned.",
                                  color=0xFF5733)
            await ctx.send(embed=embed)
            return

def setup(client):
  client.add_cog(Development(client))