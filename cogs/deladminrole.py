import discord, json
from discord.ext import commands

class Ticket6(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def deladminrole(self, ctx, role_id=None):
    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        admin_roles = data["verified-roles"]

        if role_id in admin_roles:
            index = admin_roles.index(role_id)

            del admin_roles[index]

            data["verified-roles"] = admin_roles

            with open('data.json', 'w') as f:
                json.dump(data, f)

            em = discord.Embed(
                title="Hercules Tickets",
                description=
                "You have successfully removed `{}` from the list of roles that get pinged when new tickets are created."
                .format(role.name),
                color=0x00a8ff)

            await ctx.send(embed=em)

        else:
            em = discord.Embed(
                title="Hercules Tickets",
                description=
                "That role isn't getting pinged when new tickets are created!",
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
  client.add_cog(Ticket6(client))