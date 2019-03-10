import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import requests



Client = discord.Client()
client = commands.Bot(command_prefix = "-")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')	


@client.event
async def on_message(message):
	if message.content.upper().startswith('-SAY'):
	 if message.author.id == "399567243744116738" or message.author.id == "293447483818901504":
			args = message.content.split(" ")
			await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
			await client.delete_message(message)

	    
	if message.content.upper().startswith('-RPS'):
		a=message.content[5:]
		answers = random.randint(1,3)
		if message.content[5:] =="":
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Invalid, Choose rock/paper/scissors.")		
		elif answers == 1 and 'rock' in a: #rock
			await client.send_message(message.channel, ":large_blue_diamond: | I choose **rock** too! It's a draaaw!")
		elif answers == 1 and 'paper' in a: #rock
			await client.send_message(message.channel, ":large_blue_diamond: | I choose **rock**! You won and I lost...")	
		elif answers == 1 and 'scissors' in a: #rock
			await client.send_message(message.channel, ":large_blue_diamond: | I choose **rock**! I won and you lost...")
			
		elif answers == 2 and 'rock' in a: #paper
			await client.send_message(message.channel, ":newspaper: | I choose **paper**! I won and you lost...")
		elif answers == 2 and 'paper' in a: #paper
			await client.send_message(message.channel, ":newspaper: | I choose **paper** too! It's a draaaw!")	
		elif answers == 2 and 'scissors' in a: #paper
			await client.send_message(message.channel, ":newspaper: | I choose **paper**! You won and I lost...")
			
		elif answers == 3 and 'rock' in a: #scissors
			await client.send_message(message.channel, ":scissors: | I choose **scissors**! You won and I lost...")
		elif answers == 3 and 'paper' in a: #scissors
			await client.send_message(message.channel, ":scissors: | I choose **scissors**! I won and you lost...")	
		elif answers == 3 and 'scissors' in a: #scissors
			await client.send_message(message.channel, ":scissors: | I choose **scissors** too! It's a draaaw!")
		
		else:
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Invalid, choose rock/paper/scissors.")	
			

			
			

	if message.content.upper().startswith('-8BALL'):
		if message.content[7:] =="":
			await client.send_message(message.channel, ":8ball: | Missing required argument - question.")
		else:
			ans = True
			while ans:
				answers = random.randint(1,8)
				if answers == 1:
					await client.send_message(message.channel, ":8ball:| It is certain.")
					break
    
				elif answers == 2:
					await client.send_message(message.channel, ":8ball: | Outlook good.")
					break
    
				elif answers == 3:
					await client.send_message(message.channel, ":8ball: | You may rely on it.")
					break
    
				elif answers == 4:
					await client.send_message(message.channel, ":8ball: | NO U!")
					break
    
				elif answers == 5:
					await client.send_message(message.channel, ":8ball: | Concentrate and ask again.")
					break
    
				elif answers == 6:
					await client.send_message(message.channel, ":8ball: | Reply hazy, try again.")
					break
    
				elif answers == 7:
					await client.send_message(message.channel, ":8ball: | My reply is no.")
					break
    
				elif answers == 8:
					await client.send_message(message.channel, ":8ball: | My sources say no.")
					break
		
		

	if message.content.upper().startswith('-FLIP'):
		a=message.content[5:]
		answers = random.randint(1,2)
		if message.content[5:] =="":
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Invalid, choose heads/tails.")		
		elif answers == 1 and 'heads' in a: #heads
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Heads. \n\nNice guess!", inline=False)
			embed.set_thumbnail(url='http://www.thesaint-online.com/wp-content/uploads/2017/04/pound-coin-front.png')
			await client.send_message(message.channel, embed=embed)			
		elif answers == 1 and 'tails' in a: #heads
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Heads. \n\nBetter luck next time...", inline=False)
			embed.set_thumbnail(url='http://www.thesaint-online.com/wp-content/uploads/2017/04/pound-coin-front.png')
			await client.send_message(message.channel, embed=embed)
		elif answers == 2 and 'tails' in a: #tails
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Tails. \n\nNice guess!", inline=False)
			embed.set_thumbnail(url='https://www.chards.co.uk/media/blog/46/2008onepoundrev500.png')
			await client.send_message(message.channel, embed=embed)
		elif answers == 2 and 'heads' in a: #tails
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Tails. \n\nBetter luck next time...", inline=False)
			embed.set_thumbnail(url='https://www.chards.co.uk/media/blog/46/2008onepoundrev500.png')
			await client.send_message(message.channel, embed=embed)	

		else:
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Invalid, choose heads/tails.")
		

			

	if message.content.startswith('-help all'): 
		embed = discord.Embed(title=':scroll: __All Commands__',description='', color=0xFF8C00)
		embed.add_field(name="-ping", value="Pings the bot.", inline=False)
		embed.add_field(name="-time", value="Current time in UK.", inline=False)
		embed.add_field(name="-mute", value="Mute a member so they cannot type or speak.", inline=False)
		embed.add_field(name="-ban", value="Ban a member.", inline=False)
		embed.add_field(name="-kick", value="Kick a member", inline=False)
		embed.add_field(name="-purge", value="Delete a number of messages from a channel", inline=False)
		embed.add_field(name="-add", value="Adds the two entered numbers.", inline=False)
		embed.add_field(name="-sub", value="Subtracts the two entered numbers.", inline=False)
		embed.add_field(name="-multi", value="Multiplies the two entered numbers.", inline=False)
		embed.add_field(name="-div", value="Divides the two entered numbers.", inline=False)
		embed.add_field(name="-choose", value="Chooses one option from the list.", inline=False)
		embed.add_field(name="-rps", value="To play rock/paper/scissors with the bot.", inline=False)
		embed.add_field(name="-flip", value="To filp a coin.", inline=False)
		embed.add_field(name="-meme", value="Displays a random meme.", inline=False)
		embed.add_field(name="-kill", value="Kills the mentioned user.", inline=False)
		embed.add_field(name="-8ball", value="Answers your yes/no questions.", inline=False)
		embed.add_field(name="-avatar", value=" Displays the avatar of the mentioned user.", inline=False)
		embed.add_field(name="-userinfo", value="Displays the mentioned users info.", inline=False)
		embed.add_field(name="-serverinfo", value="Displays the server stats.", inline=False)
		embed.add_field(name="-credits", value="Displays the bot's info.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help') and message.content[5:] =="": 
		embed = discord.Embed(title=":scroll:__BFL Help__",description='', color=0xFF8C00)
		embed.add_field(name="-help all", value="Shows the help message for all the categories.", inline=False)
		embed.add_field(name="-help general", value="Shows the general commands.", inline=False)
		embed.add_field(name="-help moderator", value="Shows the moderator commands.", inline=False)
		embed.add_field(name="-help games", value="Shows all commands related to the games.", inline=False)
		embed.add_field(name="-help math", value="Shows all commands related to math.", inline=False)
		embed.add_field(name="-help fun", value="Shows the commands for fun.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)
	
	if message.content.startswith('-help games'): 
		embed = discord.Embed(title=':scroll: __Games__',description='', color=0xFF8C00)
		embed.add_field(name="-rps", value="-rps = To play rock/paper/scissors with the bot.", inline=False)
		embed.add_field(name="-flip", value="To filp a coin.", inline=False)
		embed.add_field(name="-8ball", value="Answers your yes/no questions.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)	
		
	if message.content.startswith('-help general'): 
		embed = discord.Embed(title=':scroll: __General__',description='', color=0xFF8C00)
		embed.add_field(name="-ping", value="Pings the bot.", inline=False)
		embed.add_field(name="-time", value="Current time in UK.", inline=False)
		embed.add_field(name="-avatar", value="Displays the avatar of the mentioned user.", inline=False)
		embed.add_field(name="-about", value="Displays the bot's info.", inline=False)
		embed.add_field(name="-info", value="Displays the mentioned users info.", inline=False)
		embed.add_field(name="-server", value="Displays the server stats.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)	
		
	if message.content.startswith('-help moderator'): 
		embed = discord.Embed(title=':scroll: __Moderator__',description='', color=0xFF8C00)
		embed.add_field(name="-mute", value="Mute a member so they cannot type or speak.", inline=False)
		embed.add_field(name="-ban", value="Ban a member.", inline=False)
		embed.add_field(name="-kick", value="Kick a member", inline=False)
		embed.add_field(name="-purge", value="Delete a number of messages from a channel", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)	
		
	if message.content.startswith('-help math'): 
		embed = discord.Embed(title=':scroll: __Math__',description='', color=0xFF8C00)
		embed.add_field(name="-add", value="Adds the two entered numbers. ", inline=False)
		embed.add_field(name="-sub", value="Subtracts the two entered numbers.", inline=False)
		embed.add_field(name="-multi", value="Multiplies the two entered numbers.", inline=False)
		embed.add_field(name="-div", value="Divides the two entered numbers.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)		
		
	if message.content.startswith('-help fun'): 
		embed = discord.Embed(title=':scroll: __Fun__',description='', color=0xFF8C00)
		embed.add_field(name="-choose", value="Chooses one option from the list.", inline=False)
		embed.add_field(name="-meme", value="Displays a random meme.", inline=False)
		embed.add_field(name="-kill", value="Kills the mentioned user.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)	
		
		
	if message.content.startswith('-suggest'):
		if message.content[9:] =="":
			await client.send_message(message.channel, '<:alphaError:468832634542227477> Error. Type in a suggestion.')
		else:
			await client.send_message(message.channel, '<:alphaSuccess:547510448464068628> {0.author.mention} Your suggestion has been sent succesfully!'.format(message))
			args = message.content.split(" ")		
			channel=client.get_channel('536932821520875530')
			
			embed = discord.Embed(title='', color=0xFFFF00)
			embed.add_field(name="__Suggestion__", value= "```%s```" % (" ".join(args[1:])), inline=False)
			embed.add_field(name="By:", value="{0.author.mention}".format(message), inline=False)
			embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/DrPt9N7Qmi_7ihz98jQBxyBLnl_gvvt4FoS3MhNBqpo/https/openclipart.org/image/2400px/svg_to_png/10515/yves-guillou-idea.png")
			a=await client.send_message(channel, embed=embed)
			await client.add_reaction(a, "👍")
			await client.add_reaction(a, "👎")
			
			
	if message.content.upper().startswith('-KILL'):
		a=message.content[6:]
		if a == "":
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Error. Mention someone to kill him.")
		else:
			list = ["{0.author.mention}".format(message) + " rips out " + a + "'s head and starts devouring on his brain cells." , "{0.author.mention}".format(message) + " decided to go to a dance party where his rival " + a + " was at. Later on, " + a +" said: 'I fucking hate this party' and " + "{0.author.mention}".format(message) + " shot him down in plain sight." , "{0.author.mention}".format(message) + " sent " + a+ "to the Sahara desert where " + a + " slowly starved to death." , "{0.author.mention}".format(message) + " found The Hammer of Thor, which explains why " +a+" became toast." , "{0.author.mention}".format(message) + " found a cancer pill, which explains how "+a+ " got cancer." , "{0.author.mention}".format(message) + " had prayed many nights to Poseidon to kill his/her mortal enemy, but he/she never thought he would send a ravenous sharknado to eat "+a+ " and their family! (and a few neighbors too)" , "{0.author.mention}".format(message) + " drowned "+a+ " in a freezing bathtub." , "{0.author.mention}".format(message) + " ordered his pet to attack " + a, "{0.author.mention}".format(message) +" Found a wand and casted 'EXPLODE' spell on " + a, "{0.author.mention}".format(message) + " pushed "+a+" into an active volcano. " , "{0.author.mention}".format(message) + " blindfolded " +a+" and took him/her to gym to kill him/her with a shotgun! " , "{0.author.mention}".format(message) +" has a particular proclivity for pyrotechnics and puts it to good use by strapping " +a+ " to a large rocket and sending him/her straight to the moon. " , "{0.author.mention}".format(message) +" shot " +a+ " with a *lazer gun*, but killed himself/herself due to the backfire." , "{0.author.mention}".format(message)+" threw "+a+" off a bridge." , "{0.author.mention}".format(message)+" helped "+ a +" fix a broken paintball gun, just to kill " + a + " with it."] 
			secure_random = random.SystemRandom()
			m=secure_random.choice(list)		
			await client.send_message(message.channel, m)




	if message.content.startswith('-help ping'):
		embed = discord.Embed(title="Command: -ping",description='**Ping Command** \n Usage: `-ping` \n Pings the bot.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help time'):
		embed = discord.Embed(title="Command: -time",description='**Time Command** \n Usage: `-time` \n Current time in UK.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help add'):
		embed = discord.Embed(title="Command: -add",description='**Add Command** \n Usage: `-add` \n Adds the two entered numbers.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help sub'):
		embed = discord.Embed(title="Command: -sub",description='**Sub Command** \n Usage: `-sub` \n Subtracts the two entered numbers. Example (-sub 10 2)', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help multi'):
		embed = discord.Embed(title="Command: -multi",description='**Multi Command** \n Usage: `-multi` \n Multiplies the two entered numbers. Example (-multi 10 2)', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help div'):
		embed = discord.Embed(title="Command: -div",description='**Div Command** \n Usage: `-div` \n Divides the two entered numbers. Example (-div 10 2)', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help choose'):
		embed = discord.Embed(title="Command: -choose",description='**Choose Command** \n Usage: `-choose` \n Chooses one option from the list. Example (-choose 1/2/3)', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help rps'):
		embed = discord.Embed(title="Command: -rps",description='**Rps Command** \n Usage: `-rps` \n To play rock/paper/scissors with the bot. Example (-rps rock)', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help flip'):
		embed = discord.Embed(title="Command: -flip",description='**Flip Command** \n Usage: `-flip` \n To flip a coin. Example (-flip heads)', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help meme'):
		embed = discord.Embed(title="Command: -meme",description='**Meme Command** \n Usage: `-meme` \n Displays a random meme.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help kill'):
		embed = discord.Embed(title="Command: -kill",description='**Kill Command** \n Usage: `-kill` \n Kills the mentioned user.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help 8ball'):
		embed = discord.Embed(title="Command: -8ball",description='**8ball Command** \n Usage: `-8ball` \n Answers your yes/no questions.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help avatar'):
		embed = discord.Embed(title="Command: -avatar",description='**Avatar Command** \n Usage: `-avatar` \n Displays the avatar of the mentioned user.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help userinfo'):
		embed = discord.Embed(title="Command: -userinfo",description='**Info Command** \n Usage: `-info` \n Displays the mentioned users info.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help serverinfo'):
		embed = discord.Embed(title="Command: -serverinfo",description='**Server Command** \n Usage: `-server` \n Displays the server stats.', color= 0xFF8C00)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help credits'):
		embed = discord.Embed(title="Command: -credits",description='**About Command** \n Usage: `-about` \n Displays the bots info.', color= 0x546E7A)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

client.run(str(os.environ.get('BOT_TOKEN')))
