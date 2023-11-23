import discord


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
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')       
        
        
    if message.content.startswith('this server is cool'):
        await message.channel.send('Thanks! We Appreciate It!')
    if message.content.startswith('This server is cool'):
        await message.channel.send('Thanks! We Appreciate It!')
    if message.content.startswith('this server is bad'):
        await message.channel.send('Oh Okay, Please Tell us Ways that we could Improve!')
    if message.content.startswith('this server is trash'):
        await message.channel.send('Oh Okay, Please Tell us Ways that we could Improve!')
        
    if message.content.startswith('This server is bad'):        
         await message.channel.send('Oh Okay, Please Tell us Ways that we could Improve!')
    if message.content.startswith('This server is trash'):
        await message.channel.send('Oh Okay, Please Tell us Ways that we could Improve!')
        
    if message.content.startswith('what is the ip'):
        await message.channel.send('The IP can be found upon creating an application. Please go to the **create application** channel, type **;apply** and wait for the bot to DM you! Then, just answer his questions, and wait for a staff member to accept! Thats It! Then, go to the **server-info** channel, and there will be the IP of both java & bedrock!')    
    if message.content.startswith('What is the ip'):
        await message.channel.send('The IP can be found upon creating an application. Please go to the **create application** channel, type **;apply** and wait for the bot to DM you! Then, just answer his questions, and wait for a staff member to accept! Thats It! Then, go to the **server-info** channel, and there will be the IP of both java & bedrock!')
    if message.content.startswith('what is the server'):
        await message.channel.send('The IP can be found upon creating an application. Please go to the **create application** channel, type **;apply** and wait for the bot to DM you! Then, just answer his questions, and wait for a staff member to accept! Thats It! Then, go to the **server-info** channel, and there will be the IP of both java & bedrock!')
    if message.content.startswith('What is the server'):
        await message.channel.send('The IP can be found upon creating an application. Please go to the **create application** channel, type **;apply** and wait for the bot to DM you! Then, just answer his questions, and wait for a staff member to accept! Thats It! Then, go to the **server-info** channel, and there will be the IP of both java & bedrock!')
    if message.content.startswith('help'):
        await message.channel.send('Oh Okay, If you need help, please make sure to **tell a staff member** about your problem!\n As for my help, I am a simple bot, I dont really have any help menus! You can try running "!help" to get help from the main bot!')
    if message.content.startswith('Help'):
        await message.channel.send('Oh Okay, If you need help, please make sure to **tell a staff member** about your problem!\n As for my help, I am a simple bot, I dont really have any help menus! You can try running "!help" to get help from the main bot!')
    if message.content.startswith('please help'):
        await message.channel.send('Oh Okay, If you need help, please make sure to **tell a staff member** about your problem!\n As for my help, I am a simple bot, I dont really have any help menus! You can try running "!help" to get help from the main bot!')
    if message.content.startswith('Please help'):
        await message.channel.send('Oh Okay, If you need help, please make sure to **tell a staff member** about your problem!\n As for my help, I am a simple bot, I dont really have any help menus! You can try running "!help" to get help from the main bot!')
    if message.content.startswith('version'):
        await message.channel.send('Java & Bedrock **1.19.2 (or .3)**')
    if message.content.startswith('Version'):
        await message.channel.send('Java & Bedrock **1.19.2 (or .3)**')
    if message.content.startswith('what is the server version'):
        await message.channel.send('Java & Bedrock **1.19.2 (or .3)**')
    if message.content.startswith('What is the server version'):
        await message.channel.send('Java & Bedrock **1.19.2 (or .3)**')
    if message.content.startswith('what is the version'):
        await message.channel.send('Java & Bedrock **1.19.2 (or .3)**')
    if message.content.startswith('What is the version'):
        await message.channel.send('Java & Bedrock **1.19.2 (or .3)**')
        
    if message.content.startswith('fuck'):
        await message.reply('Aye! Keep it PG!') 
        await msg.delete()
    if message.content.startswith('Fuck'):
        await message.reply('Aye! Keep it PG!') 
        await msg.delete()
    if message.content.startswith('piss'):
        await message.reply('Aye! Keep it PG!') 
        await msg.delete()
    if message.content.startswith('Piss'):
        await message.reply('Aye! Keep it PG!') 
        await msg.delete()
    if message.content.startswith('bitch'):
        await message.reply('Aye! Keep it PG!')
        await msg.delete()
    if message.content.startswith('Bitch'):
        await message.reply('Aye! Keep it PG!')
        await msg.delete()
    if message.content.startswith('shit'):
        await message.reply('Aye! Keep it PG!')
        await msg.delete()
    if message.content.startswith('Shit'):
        await message.reply('Aye! Keep it PG!')
        await msg.delete()
    if message.content.startswith('crap'):
        await message.reply('Aye! Keep it PG!')
        await msg.delete()
    if message.content.startswith('Crap'):
        await message.reply('Aye! Keep it PG!')
        await msg.delete()
    if message.content.startswith('arsehole'):
        await message.reply('Aye! Keep it PG!')
        await msg.delete()
    if message.content.startswith('Arsehole'):
        await message.reply('Aye! Keep it PG!')
        await msg.delete()
client.run('bot token goes here xD')
