import discord
from discord import client
from dotenv import dotenv_values
import random
import requests
import json

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
			res = get_ilvl(message=message)
			await message.channel.send(res[0]+' Your ilvl is: '+ str(res[1]))


def get_ilvl(message):
	if message.author.name == "PrisonMike" and message.author.discriminator == '5172':
		char = "aiiyuu"
		server = "kazzak"
	if message.author.name == "Bacornia" and message.author.discriminator == '2634':
		char = "chreed"
		server = "kazzak"
	if message.author.name == "Havrekakan" and message.author.discriminator == '0001':
		char = "havredh"
		server = "kazzak"
	if message.author.name == "Posez" and message.author.discriminator == '9641':
		char = "adreida"
		server = "kazzak"
	if message.author.name == "Aeico" and message.author.discriminator == '2769':
		char = "droratio"
		server = "kazzak"
	url = "https://eu.api.blizzard.com/profile/wow/character/"
	cont = server+"/"+char+"/equipment?namespace=profile-eu&locale=en_GB&access_token="+str(tokens["BLIZZARD_TOKEN"])
	res = requests.get(url+cont)
	real = res.text
	real = json.loads(real)
	sum = 0
	count = 0;
	for item in real['equipped_items']:
		sum += int(item['level']['value'])
		count += 1
	return [char, sum/count]		

if __name__ == "__main__":
	tokens = dotenv_values(".env")
	
	url = "https://eu.api.blizzard.com/profile/wow/character/"
	cont = "kazzak/chreed/equipment?namespace=profile-eu&locale=en_GB&access_token="+str(tokens["BLIZZARD_TOKEN"])
	res = requests.get(url+cont)
	real = res.text
	real = json.loads(real)
	sum = 0
	count = 0;
	for item in real['equipped_items']:
		if not (item['slot']['type'] == "TABARD" or item['slot']['type'] == "SHIRT"):
			sum += int(item['level']['value'])
			count += 1
	print(sum/count)

	client.run(tokens["DISCORD_SECRET"])
	
