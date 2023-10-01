import discord
import json

with open('keys.json') as f:
    keys = json.load(f)

TOKEN = keys['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message: discord.Message):

    # print("Guild: " + str(message.guild) + " Channel: " + str(message.channel) + " User: " + str(message.author) + " Message: " + str(message.content))

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)