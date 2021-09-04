import discord, json
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions 
client = discord.Client()

class Ticket8(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def new(self, ctx, *, args=None):

    await client.wait_until_ready()

    if args == None:
        message_content = "Please wait, we will be with you shortly!"

    else:
        message_content = "".join(args)

    with open("data.json") as f:
        data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1

    ticket_channel = await ctx.guild.create_text_channel(
        "ticket-{}".format(ticket_number))
    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id),
                                         send_messages=False,
                                         read_messages=False)

    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role,
                                             send_messages=True,
                                             read_messages=True,
                                             add_reactions=True,
                                             embed_links=True,
                                             attach_files=True,
                                             read_message_history=True,
                                             external_emojis=True)

    await ticket_channel.set_permissions(ctx.author,
                                         send_messages=True,
                                         read_messages=True,
                                         add_reactions=True,
                                         embed_links=True,
                                         attach_files=True,
                                         read_message_history=True,
                                         external_emojis=True)

    em = discord.Embed(title="New ticket from {}#{}".format(
        ctx.author.name, ctx.author.discriminator),
                       description="{}".format(message_content),
                       color=0x00a8ff)

    await ticket_channel.send(embed=em)

    pinged_msg_content = ""
    non_mentionable_roles = []

    if data["pinged-roles"] != []:

        for role_id in data["pinged-roles"]:
            role = ctx.guild.get_role(role_id)

            pinged_msg_content += role.mention
            pinged_msg_content += " "

            if role.mentionable:
                pass
            else:
                await role.edit(mentionable=True)
                non_mentionable_roles.append(role)

        await ticket_channel.send(pinged_msg_content)

        for role in non_mentionable_roles:
            await role.edit(mentionable=False)

    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)

    created_em = discord.Embed(
        title=f'Hercules Tickets',
        description="Your ticket has been created at {}".format(
            ticket_channel.mention),
        color=0x00a8ff)

    await ctx.send(embed=created_em)

def setup(client):
  client.add_cog(Ticket8(client))