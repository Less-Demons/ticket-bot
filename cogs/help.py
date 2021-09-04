import discord, json
from discord.ext import commands

class help(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def help(self, ctx):
    with open("data.json") as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if ctx.author.guild_permissions.administrator or valid_user:

        em = discord.Embed(title="Hercules Help",
                           description="",
                           color=0x00a8ff)
        em.add_field(
            name="`.close`",
            value=
            "Use this to close a ticket. This command only works in ticket channels."
        )
        em.add_field(
            name="`.addaccess <role_id>`",
            value=
            "This can be used to give a specific role access to all tickets. This command can only be run if you have an admin-level role for this bot."
        )
        em.add_field(
            name="`.delaccess <role_id>`",
            value=
            "This can be used to remove a specific role's access to all tickets. This command can only be run if you have an admin-level role for this bot."
        )
        em.add_field(
            name="`.addadminrole <role_id>`",
            value=
            "This command gives all users with a specific role access to the admin-level commands for the bot, such as `/addpingedrole` and `/addaccess`. This command can only be run by users who have administrator permissions for the entire server."
        )
        em.add_field(
            name="`.deladminrole <role_id>`",
            value=
            "This command removes access for all users with the specified role to the admin-level commands for the bot, such as `/addpingedrole` and `/addaccess`. This command can only be run by users who have administrator permissions for the entire server."
        )
        em.add_field(
            name="`.mute`",
            value=
            "This command will mute the specified user. This command can only be run by users who have kick permissions for the entire server."
        )
        em.add_field(
            name="`.unmute`",
            value=
            "This command will unmute the specified user. This command can only be run by users who have kick permissions for the entire server."
        )
        em.add_field(
            name="`.kick`",
            value=
            "This command will kick the specified user. This command can only be run by users who have kick permissions for the entire server."
        )
        em.add_field(
            name="`.ban`",
            value=
            "This command will ban the specified user. This command can only be run by users who have ban permissions for the entire server."
        )
        em.add_field(
            name="`.unban`",
            value=
            "This command will unban the specified user. This command can only be run by users who have ban permissions for the entire server."
        )
        em.add_field(
            name="`.invite`",
            value=
            "This command will give you the invite link to invite the bot to your server. This command can be run by everyone."
        )
        em.add_field(
            name="`.avatar`",
            value=
            "This command will give you the avatar of the selected person.")
        em.add_field(
            name="`.slowmode`",
            value="This command will allow you to change the slowmode.")
        em.set_footer(text="Information requested by: {}".format(
            ctx.author.display_name))

        await ctx.send(embed=em)

    else:

        em = discord.Embed(title="Hercules Tickets Help",
                           description="",
                           color=0x00a8ff)
        em.add_field(
            name="`.new <message>`",
            value=
            "This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket."
        )
        em.add_field(
            name="`.close`",
            value=
            "Use this to close a ticket. This command only works in ticket channels."
        )
        em.add_field(
            name="`.invite`",
            value=
            "This command will give you the invite link to invite the bot to your server. This command can be run by everyone."
        )
        em.add_field(
            name="`.avatar`",
            value=
            "This command will give you the avatar of the selected person.")
        em.set_footer(text="Information requested by: {}".format(
            ctx.author.display_name))

        await ctx.send(embed=em)


def setup(client):
  client.add_cog(help(client))