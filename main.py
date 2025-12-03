import discord
from discord import app_commands
import os

# Configuración básica
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f'Hemos iniciado sesión como {client.user}')

# Este es el Slash Command que te dará la insignia
@tree.command(name="ping", description="Comando para reclamar la insignia de desarrollador")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("¡Pong! Espera 24 horas y reclama tu insignia aquí: https://discord.com/developers/active-developer")

# Arrancar el bot
client.run(os.environ['DISCORD_TOKEN'])
