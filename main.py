import discord
from discord import client
from dotenv import dotenv_values
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

class JockeBot(discord.Client):
	
	@client.event
	async def on_ready():
		print(f'Logged in as {client.user}')

	@client.event
	async def on_message(message):
		if message.content == '*hi':
			await message.channel.send('Hello!')
	
	@client.event
	async def on_message(message):
		if message.content == '*commands':
			await message.channel.send('Choices are *commands and *hi!')
		
	@client.event
	async def on_message(message):
		if message.content == '*bugged':
			random_num = random.randrange(0,100)
			print(message.author)
			if message.author.name == "Aeico" and message.author.discriminator == '2769':
				await message.channel.send('The game is anything you want 10/10 <:helenaW:1066390018119184474> Rolled:'+ str(100))
				return;
			if random_num < 5:
				await message.channel.send('This time the game was not bugged :soupchamp::/ Rolled:'+ str(random_num))
			elif random_num < 20:
				await message.channel.send('Game was not bugged but closer towards maybe being bugged <a:BUSSERS:769395313563140136> Rolled:'+ str(random_num))
			elif random_num == 100:
				await message.channel.send('The game is anything you want 10/10 <:helenaW:1066390018119184474> Rolled:'+ str(random_num))
			else:
				await message.channel.send('Game was bugged <:YEP:791084125138321438> Rolled:'+ str(random_num))



if __name__ == "__main__":
	tokens = dotenv_values(".env")
	#intents = discord.Intents.default()
	#intents.message_content = True
	#jocke_bot = JockeBot(intents)
	
	client.run(tokens["DISCORD_SECRET"])
	
	print(tokens["DISCORD_PUBLIC_KEY"])
	print("hello")
