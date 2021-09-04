import discord, datetime
from discord.ext import commands

class Example(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def avatar(self, ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    icon = member.avatar_url
    em = discord.Embed(title='Avatar',
                       color=0x123456,
                       timestamp=datetime.utcnow()).set_author(
                           name=f'{member.name}#{member.discriminator}',
                           icon_url=icon).set_image(url=icon)

    await ctx.send(embed=em)

def setup(client):
  client.add_cog(Example(client))