import discord, json
from discord.ext import commands

class Ticket1(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def addaccess(self, ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:
        role_id = int(role_id)

        if role_id not in data["valid-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["valid-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(
                    title="Hercules Tickets",
                    description=
                    "You have successfully added `{}` to the list of roles with access to tickets."
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

        else:
            em = discord.Embed(
                title="Hercules Tickets",
                description="That role already has access to tickets!",
                color=0x00a8ff)
            await ctx.send(embed=em)

    else:
        em = discord.Embed(
            title="Hercules Tickets",
            description="Sorry, you don't have permission to run that command.",
            color=0x00a8ff)
        await ctx.send(embed=em)


def setup(client):
  client.add_cog(Ticket1(client))