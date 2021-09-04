import discord, json
from discord.ext import commands

class Ticket2(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def addadminrole(self, ctx, role_id=None):

    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        data["verified-roles"].append(role_id)

        with open('data.json', 'w') as f:
            json.dump(data, f)

        em = discord.Embed(
            title="Hercules Tickets",
            description=
            "You have successfully added `{}` to the list of roles that can run admin-level commands!"
            .format(role.name),
            color=0x00a8ff)
        await ctx.send(embed=em)

    except:
        em = discord.Embed(
            title="Hercules Tickets",
            description=
            "That isn't a valid role ID. Please try again with a valid role ID."
        )
        await ctx.send(embed=em)

def setup(client):
  client.add_cog(Ticket2(client))