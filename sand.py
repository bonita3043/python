import discord
from captcha.image import ImageCaptcha
import random
import time
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print("WiNer 실행")
    game = discord.Game('위너 아들')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/출근"):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                #author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0x80E12A)
                channel = 772814747238268988
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                embed.set_image(url="https://media.discordapp.net/attachments/781324193286586379/782135636488486922/Isthisacat.png")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("/퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                #author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0xFF0000)
                channel = 772814747238268988
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
                embed.set_image(url="https://media.discordapp.net/attachments/781324193286586379/782135636488486922/Isthisacat.png")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

        async def on_message(message):
            if message.content.startswith("/인증"):  # 명령어 /인증
                a = ""
                Captcha_img = ImageCaptcha()
                for i in range(6):
                    a += str(random.randint(0, 9))

                name = str(message.author.id) + ".png"
                Captcha_img.write(a, name)

                await message.channel.send(f"""{message.author.mention} 아래 숫자를 10초 내에 입력해주세요. """)
                await message.channel.send(file=discord.File(name))

                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel

                try:
                    msg = await client.wait_for("message", timeout=10, check=check)  # 제한시간 10초
                except:
                    await message.channel.purge(limit=3)
                    chrhkEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
                    chrhkEmbed.add_field(name='닉네임', value=message.author, inline=False)
                    chrhkEmbed.add_field(name='이유', value='시간초과', inline=False)
                    await message.channel.send(embed=chrhkEmbed)
                    print(f'{message.author} 님이 시간초과로 인해 인증을 실패함.')
                    return

                if msg.content == a:
                    role = discord.utils.get(message.guild.roles, name="인증")
                    await message.channel.purge(limit=4)
                    tjdrhdEmbed = discord.Embed(title='인증성공', color=0x04FF00)
                    tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
                    tjdrhdEmbed.add_field(name='5초후 인증역할이 부여됩니다.', value='** **', inline=False)
                    tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
                    await message.channel.send(embed=tjdrhdEmbed)
                    time.sleep(5)
                    await message.author.add_roles(role)
                else:
                    await message.channel.purge(limit=4)
                    tlfvoEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
                    tlfvoEmbed.add_field(name='닉네임', value=message.author, inline=False)
                    tlfvoEmbed.add_field(name='이유', value='잘못된 숫자', inline=False)
                    await message.channel.send(embed=tlfvoEmbed)
                    print(f'{message.author} 님이 잘못된 숫자로 인해 인증을 실패함.')

                async def on_message(message):
                    if message.content.startswith('/청소'):
                        try:
                            # 메시지 관리 권한 있을시 사용가능
                            if message.author.guild_permissions.manage_messages:
                                amount = message.content[4:]
                                await message.delete()
                                await message.channel.purge(limit=int(amount))
                                message = await message.channel.send(
                                    embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨',
                                                        colour=discord.Colour.green()))
                                await asyncio.sleep(2)
                                await message.delete()
                            else:
                                await message.channel.send('``명령어 사용권한이 없습니다.``')
                        except:
                            pass







client.run('NzgxNDk5MTUyNDQ5MjczODY3.X7-hzQ.99qW3AaVPcvdJCkQp-jc6FE8VPw')