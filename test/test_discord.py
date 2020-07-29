import discord
from decouple import config

class MyClient(discord.Client):
    async def on_ready(self):
        print('Bot fai iniciade :D')

    async def on_message(self, message):
        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient(config('DISCORD_BOT_TOKEN'))
client.run()
