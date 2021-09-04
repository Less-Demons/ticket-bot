import discord
from discord.ext import commands

class Miscellaneous(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def invite(self, ctx):
    embed = discord.Embed(
        title="Invite",
        url=
        "https://discord.com/api/oauth2/authorize?client_id=875244177355575306&permissions=268618870&scope=bot",
        description=
        "I am happy you are wanting to invite my bot to your server!",
        color=0xFF5733)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    embed.set_footer(
        text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Miscellaneous(client))