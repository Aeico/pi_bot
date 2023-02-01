import discord
from discord import client
from dotenv import dotenv_values
import random
import requests

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
			if message.author.name == "PrisonMike" and message.author.discriminator == '5172':
				await message.channel.send('Not this time Robin I am sorry <:Sadge:791082666782490684>')
				return;
			if random_num < 5:
				await message.channel.send('This time the game was not bugged <a:modCheck:950386916161880147>:/ Rolled:'+ str(random_num))
			elif random_num < 20:
				await message.channel.send('Game was not bugged but closer towards maybe being bugged <a:borpaSpin:827959496105918565> Rolled:'+ str(random_num))
			elif random_num == 100:
				await message.channel.send('The game is anything you want 10/10 <:helenaW:1066390018119184474> Rolled:'+ str(random_num))
			elif random_num == 69:
				await message.channel.send('Nice <:EZ:791084186688815104> Rolled:'+ str(random_num))
			else:
				await message.channel.send('Game was bugged <:YEP:791084125138321438> Rolled:'+ str(random_num))

	@client.event
	async def on_message(message):
		if message.content == '*wow':
			url = "https://eu.api.blizzard.com/profile/wow/character/"
			cont = "Kazzak/Droratio/equipment?namespace=profile-eu&locale=en_GB&access_token="+str(tokens["BLIZZARD_TOKEN"])
			requests.get(url+cont)
		

if __name__ == "__main__":
	tokens = dotenv_values(".env")
	
	

	client.run(tokens["DISCORD_SECRET"])
	
