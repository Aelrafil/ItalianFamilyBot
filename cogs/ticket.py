import disnake as discord
from disnake.ext import commands
from disnake.enums import ButtonStyle

class ticketButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Generale", custom_id="persistentView:generaleButton", style=ButtonStyle.blurple)
    async def generaleButton(self, button: discord.ui.Button, ctx: commands.Context):
        try:
            em = discord.Embed(
                title="Supporto Generale",
                description=f"{ctx.author.mention} benvenuto nell'assistenza generale,\n"
                            f"mentre attende uno staffer, descriva il suo problema,\n"
                            f"uno staffer le risponderà il prima possibile."
            )
            em.set_author(name="𝑰𝒕𝒂𝒍𝒊𝒂𝒏 𝑭𝒂𝒎𝒊𝒍𝒚", url=ctx.guild.icon.url)
            await ctx.send(embed=em)
        except:
            pass

    @discord.ui.button(label="Generale", custom_id="persistentView:candidatureButton", style=ButtonStyle.blurple)
    async def candidatureButton(self, button: discord.ui.Button, ctx: commands.Context):
        try:
            em = discord.Embed(
                title="Supporto Generale",
                description=f"{ctx.author.mention} benvenuto nelle candidature,\n"
                            f"attenda che uno staffer risponda al ticket."
            )
            em.set_author(name="𝑰𝒕𝒂𝒍𝒊𝒂𝒏 𝑭𝒂𝒎𝒊𝒍𝒚", url=ctx.guild.icon.url)
            await ctx.send(embed=em)
        except:
            pass

class ticketBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ticket-setup")
    async def ticketSetup(self, button: discord.ui.Button, inter: discord.ApplicationCommandInteraction, canale: discord.TextChannel):
        em = discord.Embed(
            title="🎟️Ticket🎟️",
            description="Apri un ticket:"
        )
        em.set_author(name="𝑰𝒕𝒂𝒍𝒊𝒂𝒏 𝑭𝒂𝒎𝒊𝒍𝒚", url=inter.guild.icon.url)
        await canale.send(embed=em)