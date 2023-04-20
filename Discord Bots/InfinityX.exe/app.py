import discord
import random
import asyncio
import typing

from discord.ext import tasks
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
        
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1019245565697065053)
    await channel.send(f'Welcome {member.mention} to the server!')
            
@commands.command()
async def ip(ctx):
    await ctx.send("The IP can be found upon creating an application. Please Go to https://discord.com/channels/941222379496013844/1074212997750345828 and click the **blue button**. Then, fill the form, and, thats it! The IP then should be in https://discord.com/channels/941222379496013844/941225197514661928")
@commands.command()
async def version(ctx):
    await ctx.send("Java & Bedrock **1.19.4)**")
@commands.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')    
@commands.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
    
@commands.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')
    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()
    answer = random.randint(1, 10)
    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Sorry, you took too long it was {answer}.')
    if int(guess.content) == answer:
        await ctx.send('You are right!')
    else:
        await ctx.send(f'Oops. It is actually {answer}.')
    
    
    
    
    
@commands.command()
async def userinfo(ctx: commands.Context, user: discord.User):
    # In the command signature above, you can see that the `user`
    # parameter is typehinted to `discord.User`. This means that
    # during command invocation we will attempt to convert
    # the value passed as `user` to a `discord.User` instance.
    # The documentation notes what can be converted, in the case of `discord.User`
    # you pass an ID, mention or username (discrim optional)
    # E.g. 80088516616269824, @Danny or Danny#0007

    # NOTE: typehinting acts as a converter within the `commands` framework only.
    # In standard Python, it is use for documentation and IDE assistance purposes.

    # If the conversion is successful, we will have a `discord.User` instance
    # and can do the following:
    user_id = user.id
    username = user.name
    avatar = user.display_avatar.url
    await ctx.send(f'User found: {user_id} -- {username}\n{avatar}')


@userinfo.error
async def userinfo_error(ctx: commands.Context, error: commands.CommandError):
    # if the conversion above fails for any reason, it will raise `commands.BadArgument`
    # so we handle this in this error handler:
    if isinstance(error, commands.BadArgument):
        return await ctx.send('Couldn\'t find that user.')



# Custom Converter here
class ChannelOrMemberConverter(commands.Converter):
    async def convert(self, ctx: commands.Context, argument: str):
        # In this example we have made a custom converter.
        # This checks if an input is convertible to a
        # `discord.Member` or `discord.TextChannel` instance from the
        # input the user has given us using the pre-existing converters
        # that the library provides.

        member_converter = commands.MemberConverter()
        try:
            # Try and convert to a Member instance.
            # If this fails, then an exception is raised.
            # Otherwise, we just return the converted member value.
            member = await member_converter.convert(ctx, argument)
        except commands.MemberNotFound:
            pass
        else:
            return member

        # Do the same for TextChannel...
        textchannel_converter = commands.TextChannelConverter()
        try:
            channel = await textchannel_converter.convert(ctx, argument)
        except commands.ChannelNotFound:
            pass
        else:
            return channel

        # If the value could not be converted we can raise an error
        # so our error handlers can deal with it in one place.
        # The error has to be CommandError derived, so BadArgument works fine here.
        raise commands.BadArgument(f'No Member or TextChannel could be converted from "{argument}"')


@commands.command()
async def notify(ctx: commands.Context, target: ChannelOrMemberConverter):
    # This command signature utilises the custom converter written above
    # What will happen during command invocation is that the `target` above will be passed to
    # the `argument` parameter of the `ChannelOrMemberConverter.convert` method and
    # the conversion will go through the process defined there.

    await target.send(f'Hello, {target.name}!')


@commands.command()
async def ignore(ctx: commands.Context, target: typing.Union[discord.Member, discord.TextChannel]):
    # This command signature utilises the `typing.Union` typehint.
    # The `commands` framework attempts a conversion of each type in this Union *in order*.
    # So, it will attempt to convert whatever is passed to `target` to a `discord.Member` instance.
    # If that fails, it will attempt to convert it to a `discord.TextChannel` instance.
    # See: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#typing-union
    # NOTE: If a Union typehint converter fails it will raise `commands.BadUnionArgument`
    # instead of `commands.BadArgument`.

    # To check the resulting type, `isinstance` is used
    if isinstance(target, discord.Member):
        await ctx.send(f'Member found: {target.mention}, adding them to the ignore list.')
    elif isinstance(target, discord.TextChannel):  # this could be an `else` but for completeness' sake.
        await ctx.send(f'Channel found: {target.mention}, adding it to the ignore list.')
@commands.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@commands.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@commands.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@commands.command()
async def repeat1(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@commands.command()
async def repeat2(ctx, times: int, content='Anyone Free to Play on the Server?'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

#HEREHERHEAKDAHDLIHASIUDHAISUHDIUASHDIHASIHUSAHDUHASDI
@commands.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
@commands.command()
async def procedure(ctx, member: discord.Member):
    await ctx.send(f'{member.mention}, The Procedure to join the server is simple! Go to https://discord.com/channels/941222379496013844/1074212997750345828IP and click on the blue button. Then, just fill the form, and that it! The IP wil be in will be in https://discord.com/channels/941222379496013844/941225197514661928ℹ ')




@commands.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


# Built-in type converters.
@commands.command()
async def multiply(ctx: commands.Context, number: int, maybe: bool):
    # We want an `int` and a `bool` parameter here.
    # `bool` is a slightly special case, as shown here:
    # See: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#bool

    if maybe is True:
        return await ctx.send(number * 2)
    await ctx.send(number * 5)





bot.add_command(userinfo)
bot.add_command(notify)
bot.add_command(ignore)
bot.add_command(add)
bot.add_command(roll)
bot.add_command(choose)
bot.add_command(repeat1)
bot.add_command(repeat2)
bot.add_command(joined)
bot.add_command(cool)
bot.add_command(multiply)
bot.add_command(ping)
bot.add_command(ip)
bot.add_command(version)
bot.add_command(guess)
bot.add_command(procedure)
bot.add_command(kick)


#client = MyClient(intents=intents)
bot.run('MTAzMDUxNDE3NTg4MzEwNDI5Ng.GeqhjR.wQzrot_NeRxe-o_WiBUSKpi4IIy42SCxg353W8')
