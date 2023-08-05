import disnake as discord
from disnake.ext import commands
from disnake.enums import ButtonStyle

class verifyButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verificati", custom_id="peristentView:verifyButton", style=ButtonStyle.green)
    async def verifyButton(self, button: discord.ui.Button, ctx: commands.Context):
        role = ctx.guild.get_role(1136383971337457745)

        if role in ctx.author.roles:
            await ctx.send("Sei già verificato.")
        else:
            em = discord.Embed(
                title="🛡️Verifica🛡️",
                description="Ti sei verificato con successo.",
                color=discord.Color.blurple()
            )
            em.set_author(name="𝑰𝒕𝒂𝒍𝒊𝒂𝒏 𝑭𝒂𝒎𝒊𝒍𝒚", url=ctx.guild.icon.url)
            await ctx.send(embed=em, delete_after=5)




class verifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="verify-setup")
    async def verifySetup(self, inter: discord.ApplicationCommandInteraction, canale: discord.TextChannel):
        em = discord.Embed(
            title="🛡️Verifica🛡️",
            description="Premi il bottone\n"
                        "per accede a tutti i canali.",
            color=discord.Color.blurple()
        )
        em.set_author(name="𝑰𝒕𝒂𝒍𝒊𝒂𝒏 𝑭𝒂𝒎𝒊𝒍𝒚", url=inter.guild.icon.url)
        await canale.send(embed=em, view=verifyButton())
