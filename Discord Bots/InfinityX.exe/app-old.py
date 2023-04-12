import discord
 from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
    if message.content.startswith('Hi'):
        await message.channel.send('Hello!')
    if message.content.startswith('this server is cool'):
        await message.channel.send('Thanks! We Appreciate It!')
    if message.content.startswith('this server is bad'):
        await message.channel.send('Oh Okay, Please Tell us Ways that we could Improve!')
    if message.content.startswith('this server is trash'):
        await message.channel.send('Oh Okay, Please Tell us Ways that we could Improve!')
    if message.content.startswith('what is the ip'):
        await message.channel.send('The IP can be found upon creating an application. Please go to the **create application** channel, type **;apply** and wait for the bot to DM you! Then, just answer his questions, and wait for a staff member to accept! Thats It! Then, go to the **server-info** channel, and there will be the IP of both java & bedrock!')    
        
client.run('MTAzMDUxNDE3NTg4MzEwNDI5Ng.GeqhjR.wQzrot_NeRxe-o_WiBUSKpi4IIy42SCxg353W8')




