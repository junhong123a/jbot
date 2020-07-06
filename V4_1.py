from pymongo import MongoClient
import discord
import asyncio
from discord.utils import get
import pymongo
import random
import threading
import time
import ast
import bs4
import openpyxl
from itertools import cycle
import re
import os
from urllib.request import urlopen, Request
import urllib
import datetime
import json
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import ctx
import sys

logchannel = 727388709485543485
errorchannel = 727388190549475400
owner = [447934468603379724]
botjoinchannel = 695243394729115668
readylog = 727388158232232031
botleavelog = 697773473161936959
gunlog = 727388605516873790
id = 503502157925056514
ban = [604617640891121664]

# connection = pymongo.MongoClient(mongo_server, 27017)

start_time = time.time()

token = "NTAzNTAyMTU3OTI1MDU2NTE0.Xv9c8A.2mSViA-bI_vI2ZUbPvoze5qTt_w"

client = MongoClient('localhost', 27017)
db = client['test_database']
client = discord.Client()
game = discord.Game("준홍아 도움")     


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(id)
    await client.get_channel(readylog).send("준홍봇 전원 on")
    dagi = 8
    messages = ['준홍아 도움을 입력해 명령어 확인', f'{len(client.guilds)}개의 서버에 참여중', f'{len(client.users)}명의 유저들과 소통하는중', '준홍!good good & 잊니 유튜브 채널 디스코드 를 가입하세요!', '문의는 junhong123a@naver.com 또는 준홍!good good#8922', '개인메세지는 `준홍아 갠챗`', '사용자 여러분 감사합니다!', f'이 메세지는 {dagi}초마다 바뀝니다.']
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(dagi)
       
@client.event
async def on_message(message):
    try:
        if message.author.bot:                 
            return None

        #banlist=['output','token', 'file=', 'os', 'logout', 'login', 'quit', 'exit', 'sys', 'shell','dir']
        #for banword in banlist:
            #if banword in message.content:
                #return None

        if message.content.startswith('준홍아'):
            await client.get_channel(int(logchannel)).send(f'guild : {message.channel.guild}({message.guild.id})\nch = {message.channel.name}({message.channel.id})\nauthor = {message.author}({message.author.id})\ncontent = {message.content}')

            if message.content == "준홍아 안녕":
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                await message.channel.send(f"<@{message.author.id}> 님 환영합니다!")
                embed.add_field(name="준홍봇 채팅기능", value="안녕하세요 준홍봇입니다. 준홍봇의 개발자는 준홍!good good#8922입니다.! 자세한 명령어는 `준홍아 도움 `을! \n그리고 왠만하면 봇DM에서 명령어는 사용안해주셨으면 합니다." , inline=True)
                embed.add_field(name="안내사항", value="준홍봇의 개발자 준홍은 봇 도우미로 활동하고 있습니다. 도움이 필요하신분은 준홍!good good#8922로 DM  주시거나 010 - 4991 - 5446번 준홍에게 연락주시기 바랍니다", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                    
            elif message.content  ==  '준홍아 핑':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(client.latency * 1000)}ms입니다!', inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                print(f'ping is {round(client.latency * 1000)}ms')

            elif message.content  ==  '준홍아 수현':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="수현은 저랑 같이 봇 개발하는 개발자 입니다", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)


            elif message.content == '준홍아 도움':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="보내는중..", value="잠시 기다려 주세요", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                time.sleep(3)
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="안녕하세요! 명령어들 앞에는 `준홍아` 라는 칭호가 붙어요 ", value="도움말 시작", inline=True)
                embed.add_field(name="준홍봇 도움말", value='애교해봐,밴,승현,내프사,안녕,감자칩,뮈해,핑,수현,갠챗 갠챗형식 : 준홍아 갠챗 유저ID 할말 ,네집,서버,찬반투표 찬반투표 형식 : 준홍아 찬반투표 ', inline=True)
                embed.add_field(name="도움말2", value="투표이름,멜론차트,개발코드,죽어,Error,Mee6,미쳤나,빼에에엑,규카츠,RST,WCDMA,주사위,짜장면,초대링크,주소들,삼해트,서버,개발코드,익명 익명형식: 준홍아 익명 메세지 ,닉네임, 정보, 탕수육,건의 건의형식 : 준홍아 건의 건의내용, 청소, 뒤져", inline=True)
                embed.add_field(name="도움말3", value="say,esay esay,say 형식: 준홍아 (e)say 할말,현재시각, 계산기, 업타임", inline=False)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.author.send(embed=embed)

            elif message.content  ==  '준홍아 죽어':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="시러요", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content.startswith('준홍아 say'):
                sms = message.content[8:]
                await message.channel.send

            elif message.content.startswith('준홍아 esay'):
                sms = message.content[9:]
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value=(sms), inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content.startswith('준홍아 갠챗'):
                author = message.guild.get_member(int(message.content[7:25]))
                msg = message.content[26:]
                #value=message.author.name
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 전송기능", value=msg, inline=True)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await author.send(embed=embed)
                await message.delete()
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 전송기능", value=f'{author}님께 갠챗 전송이 완료되었습니다!', inline=True)
                embed.set_footer(text=f"{message.author} 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content  ==  '준홍아 네집':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="준홍봇의 집은 준홍!good good&. 잊니 유튜브 채널 서버에요!!", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content.startswith('준홍아 찬반투표'):
                lern=message.content[9:]
                embed=discord.Embed(
                    title=str(lern),
                    description=f"{message.author.display_name}님의 찬반투표"
                )
                msg=await message.channel.send(embed=embed)
                await msg.add_reaction('👍')
                await msg.add_reaction('👎')

            elif message.content=='준홍아 멜론차트':
                if __name__=="__main__":
                    RANK=10
                    header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
                    req = requests.get('https://www.melon.com/chart/index.htm', headers = header)
                    html = req.text
                    parse = BeautifulSoup(html, 'html.parser')
                    titles = parse.find_all("div", {"class": "ellipsis rank01"})
                    songs = parse.find_all("div", {"class": "ellipsis rank02"})
                    title = []
                    song = []
                    embed=discord.Embed(
                        title="멜론차트 상위권(1~10위)\n차트 출처 : kakao(melon)\n", 
                        colour=0x85CFFF, timestamp=message.created_at
                    )
                    for t in titles:
                        title.append(t.find('a').text)
                    for s in songs:
                        song.append(s.find('span', {"class": "checkEllipsis"}).text)
                    for i in range(RANK):
                        embed.add_field(name='%3d위'%(i+1), value='%s - %s'%(title[i], song[i]), inline=False)
                    embed.set_footer(icon_url=message.author.avatar_url, text=f'{message.author}')
                    await message.channel.send(f'<@{message.author.id}>', embed=embed)

            elif message.content.startswith('준홍아 익명'):
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 문의기능", value="익명으로 문의가 완료되었습니다!", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                mes = message.content
                index = mes[4:]
                embedadmin = discord.Embed(title = index,description = "보낸사람 <@%s>" %(str(message.author.id)))
                channelid = 727388627486769193  #글이 작성되는 채널
                adminch = 727388627486769193 # 보낸사람이 누군지 확인할수있는 채널id
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="익명메세지", value=(index), inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await client.get_channel(channelid).send(embed=embed)
                await client.get_channel(adminch).send(embed=embedadmin)


            elif message.content.startswith('준홍아 내정보'):
                date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
                status_dict: dict = {discord.Status.online: '<:1_:599936558883143683> 온라인',
                    discord.Status.offline: '<:offline:599936559034269697> 오프라인',
                    discord.Status.idle: "<:2_:599936558937931777> 자리비움",
                    discord.Status.do_not_disturb: "<:3_:599936559072018433> 방해금지"}
                user_status = status_dict[message.author.status]
                roles=[role for role in message.author.roles]
                embed=discord.Embed(colour=message.author.color, timestamp=message.created_at)
                embed.set_author(name=f"유저정보 - {message.author}")
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.set_footer(text=f"{message.author},인증됨 ", icon_url=message.author.avatar_url)
                embed.add_field(name="아이디", value=f"{message.author.id}", inline=False)
                embed.add_field(name="닉네임", value=f"{message.author.display_name}", inline=False)
                embed.add_field(name="가입일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                embed.add_field(name="가장 높은 역할", value=f"{message.author.top_role.mention}", inline=False)
                embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                embed.set_footer(text=f"{message.author}, 인증됨 ", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 내프사':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 유저정보", value="유저의 프로필 사진입니다!", inline=True)
                embed.set_image(url=message.author.avatar_url)
                embed.set_footer(text=f"{message.author}, 인증됨 ", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 섭정보':
                rnrrk = message.guild.region
                print(message.guild.region)
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"서버 정보 - {message.guild.name}")
                embed.set_thumbnail(url=message.guild.icon_url)
                embed.add_field(name="서버 이름", value=message.guild.name, inline=False)
                embed.add_field(name="서버 ID", value=message.guild.id, inline=False)
                embed.add_field(name="서버 위치", value=rnrrk, inline=False)
                embed.add_field(name="서버 주인", value=f'<@{message.guild.owner.id}>', inline=False)
                embed.add_field(name="서버 주인 ID", value=message.guild.owner.id, inline=False)
                embed.add_field(name="서버 멤버 수", value=f'{len(message.guild.members)}명 (봇 : {len(list(filter(lambda x: x.bot, message.guild.members)))}명 | 유저 : {len(list(filter(lambda x: not x.bot, message.guild.members)))}명)', inline=False)
                embed.add_field(name="서버 채널 수", value=f'전체 채널: {len(message.guild.channels)}개 (채팅채널 : {len(message.guild.text_channels)}개 | 음성채널 : {len(message.guild.voice_channels)}개 | 카테고리 : {len(message.guild.categories)}개)', inline=False)
                embed.add_field(name="서버 부스트 레벨", value=f'<:boost:689765177532612648> {message.guild.premium_tier}레벨', inline=False)
                embed.add_field(name="서버 부스트 횟수", value=f'<:boost:689765177532612648> {message.guild.premium_subscription_count}번', inline=False)
                if message.guild.afk_channel != None:
                    embed.add_field(name = f'잠수 채널', value = f'<a:yes:690124935179272211> 잠수 채널이 있습니다.\n{message.guild.afk_channel.name} (타이머: {message.guild.afk_timeout})', inline = False)
                else:
                    embed.add_field(name="잠수 채널", value="<a:no:690124433406558208> 잠수 채널이 없습니다.")
                if message.guild.system_channel != None:
                    embed.add_field(name = f'시스템 채널', value = f'<a:yes:690124935179272211> 시스템 채널이 있습니다.\n<#{message.guild.system_channel.id}>', inline = False)
                else:
                    embed.add_field(name="잠수 채널", value="<a:no:690124433406558208> 시스템 채널이 없습니다.")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content.startswith('준홍아 건의'):
                msg = message.content[7:]
                await message.delete()
                await message.channel.send('건의가 완료되었어요!')
                await client.get_channel(int(gunlog)).send(f'{message.author}({message.author.id})님의 건의 : {msg}')

            elif message.content  ==  '준홍아 심심해':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="심심해?", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content  ==  '준홍아':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="왜", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content  ==  '준홍아 유튜브':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="유튜브 링크 : 준홍!good good https://www.youtube.com/channel/UCd-1tvBhwKmtvFTNiVUuLmg?view_as=subscriber, 잊니 : https://www.youtube.com/channel/UCH-t6Zw7rR2CjXPTgH7m9Kw", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content  ==  '준홍아 ㅎㅇ':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="ㅎㅇ", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content  ==  '준홍아 Error':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="Error발생! 삐삐삐ㅅㄱ", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content  ==  '준홍아 Mee6':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="mee6.xyz", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                        
            elif message.content  ==  '준홍아 미쳤나':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="아니요 도 쳤어요.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 빼에에엑':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="뻬에에에에에ㅔㄱ", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            
            elif message.content == '준홍아 주사위':
                dice = random.randint(1, 6)
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value=(dice), inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            
            elif message.content == '준홍아 규카츠':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA0MDlfOTgg%2FMDAxNTIzMjQ4NTQxOTgy.27rWawoPnQujw6HS4nPxcYjsbdZYnq-Ml3w0Q9DA3ggg.ECeoJu1W2ZiaWM8GvnPKGUylujeSjddKzkVMHZ1MuSYg.JPEG.creamy0080%2F12.%25B4%25EB%25C0%25FC%25C1%25DF%25BE%25D3%25BF%25AA%25B8%25C0%25C1%25FDDSC03358..jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            
            elif message.content == '준홍아 RST':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="아두이노에서 RESET을 담당하는 포트", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 WCDMA':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="와이드밴드 코드분할 다중접속기술, wideband code division multiple access", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 짜장면':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="http://post.phinf.naver.net/MjAxNzEyMDVfMTgx/MDAxNTEyNDUzODM1Nzgz.oLCRrLmG048QINV4T7flJ1n5whWnMgXe2FPzjD8wvMog.1fVLRKcFZlnTg3DYFO8wrGnW9wZyZpx7Yd8hkGG3RTsg.JPEG/IIh6-J6mXMeGwnXBKX2yJP5ooR_0.jpg")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 주소들':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="초대 링크https://discordapp.com/oauth2/authorize?client_id=503502157925056514&scope=bot       입니다", inline=True)
                embed.add_field(name="링크2", value="서버 링크 https://discord.gg/cgMmvmN   입니다", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            
            elif message.content == '준홍아 삼해트':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="삼해트 바보 멍청이", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            
            elif message.content == '준홍아 개발코드':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value='파이썬으로 개발됬어요!', inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 닉네임':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value=f"{message.author.display_name} 입니다.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 discord_api':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value='뭐 어쩌라고에?', inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content.startswith('준홍아 청소'):
                if message.author.id in owner:
                    varrr=message.content.split(' ')
                    await message.channel.purge(limit=int(varrr[2])+1)
                    now=datetime.datetime.now()
                    msg=await message.channel.send(embed=discord.Embed(title=f'메시지 {str(int(varrr[2]))}개 삭제 완료!', descirption='응용 기능',timestamp=message.created_at, colour=discord.Colour.blue()).set_footer(icon_url=message.author.avatar_url, text=f'{str(message.author)}, 인증됨'))
                    await asyncio.sleep(3)
                    await msg.delete()
                else:
                    await message.channel.send('뭐하시는거죠')

            elif message.content.startswith('준홍아 정보'):
                if str(message.content[7:]) == '':
                    user = message.author
                    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                    status_dict: dict = {discord.Status.online: '<:status_online:707783912121696256> 온라인',
                        discord.Status.offline: '<:status_offline:707783990953771069> 오프라인',
                        discord.Status.idle: "<:status_idle:707783934095917106> 자리비움",
                        discord.Status.do_not_disturb: "<:status_dnd:707783959634903110> 방해금지"}
                    user_status = status_dict[user.status]
                    if not len(message.author.roles) == 1:
                        roles = [role for role in user.roles]
                        embed=discord.Embed(colour=message.author.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                    else:
                        embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"유저정보 - {user}")
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    embed.add_field(name="아이디", value=f"{user.id}", inline=False)
                    embed.add_field(name="닉네임", value=f"{user.display_name}", inline=False)
                    embed.add_field(name="가입일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                    try:
                        embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                        embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                    except:
                        embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                    embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                    await message.channel.send(embed=embed)
                else:
                    try:
                        user = message.guild.get_member(int(message.content.split('<@!')[1].split('>')[0]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:707783912121696256> 온라인',
                                discord.Status.offline: '<:status_offline:707783990953771069> 오프라인',
                                discord.Status.idle: "<:status_idle:707783934095917106> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:707783959634903110> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"유저정보 - {user}")
                            else:
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                            embed.set_thumbnail(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            embed.add_field(name="아이디", value=f"{user.id}", inline=False)
                            embed.add_field(name="닉네임", value=f"{user.display_name}", inline=False)
                            embed.add_field(name="가입일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                            try:
                                embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                                embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                            except:
                                embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                            embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:707783912121696256> 온라인',
                                discord.Status.offline: '<:status_offline:707783990953771069> 오프라인',
                                discord.Status.idle: "<:status_idle:707783934095917106> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:707783959634903110> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=message.author.color, timestamp=message.created_at, title=f"봇정보 - {user}")
                            else:
                                embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"봇정보 - {user}")
                            embed.set_thumbnail(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            embed.add_field(name="봇 아이디", value=f"{user.id}", inline=False)
                            embed.add_field(name="봇 닉네임", value=f"{user.display_name}", inline=False)
                            embed.add_field(name="봇 생성일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                            try:
                                embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                                embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                            except:
                                embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                            embed.add_field(name="현재 봇 상태", value=f"{user_status}", inline=False)
                            embed.add_field(name="봇 초대링크 (관리자 권한)", value=f"[초대하기](https://discordapp.com/oauth2/authorize?client_id={user.id}&scope=bot&permissions=8)", inline=False)
                            await message.channel.send(embed=embed)
                    except:
                        user = message.guild.get_member(int(message.content.split('<@')[1].split('>')[0]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:707783912121696256> 온라인',
                                discord.Status.offline: '<:status_offline:707783990953771069> 오프라인',
                                discord.Status.idle: "<:status_idle:707783934095917106> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:707783959634903110> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"유저정보 - {user}")
                            else:
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                            embed.set_thumbnail(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            embed.add_field(name="아이디", value=f"{user.id}", inline=False)
                            embed.add_field(name="닉네임", value=f"{user.display_name}", inline=False)
                            embed.add_field(name="가입일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                            try:
                                embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                                embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                            except:
                                embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                            embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:707783912121696256> 온라인',
                                discord.Status.offline: '<:status_offline:707783990953771069> 오프라인',
                                discord.Status.idle: "<:status_idle:707783934095917106> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:707783959634903110> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=message.author.color, timestamp=message.created_at, title=f"봇정보 - {user}")
                            else:
                                embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"봇정보 - {user}")
                            embed.set_thumbnail(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            embed.add_field(name="봇 아이디", value=f"{user.id}", inline=False)
                            embed.add_field(name="봇 닉네임", value=f"{user.display_name}", inline=False)
                            embed.add_field(name="봇 생성일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                            try:
                                embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                                embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                            except:
                                embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                            embed.add_field(name="현재 봇 상태", value=f"{user_status}", inline=False)
                            embed.add_field(name="봇 초대링크 (관리자 권한)", value=f"[초대하기](https://discordapp.com/oauth2/authorize?client_id={user.id}&scope=bot&permissions=8)", inline=False)
                            await message.channel.send(embed=embed)

            elif message.content == '준홍아 탕수육':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20130412_259%2Froyalrate7_1365760080337VvTgW_JPEG%2FDSCN7945.jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 감자칩':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzEyMTJfMjA4%2FMDAxNTEzMDc4MjgwMjE5.B5xVKAl3CNo8jaYf0trsO8Wr_8XfJJRjmwn8rO6VNM0g.I5dfl1H7vyDdeK0C0xAx7cNaRyIkEYvzed3gJRhxTGgg.JPEG.changuk1225%2F%25BD%25BA%25C6%25E4%25C0%25CE_%25C6%25E4%25C0%25CE%25C6%25AE%25C5%25EB_%25B0%25A8%25C0%25DA%25C4%25A8_%25BA%25B8%25B4%25D2%25B6%25F3%25B0%25A8%25C0%25DA%25C4%25A8_5.jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 뭐해':
                a=random.randint(1,2)
                if a == 1:
                     embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                     embed.add_field(name="준홍봇 채팅기능", value="나? 수현이랑 놀거나  준홍 괴롭히지 ㅎㅎㅎㅎ", inline=True)
                     embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                     await message.channel.send(embed=embed)
                if a == 2:
                     embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                     embed.add_field(name="준홍봇 채팅기능", value="준홍에게 개발 이라는 고문을 받..죄송합니다. 사실 노는중임ㅋㅋ", inline=True)
                     embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                     await message.channel.send(embed=embed)

            elif message.content == '준홍아 star':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="star 잘생김", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content.startswith('준홍아 Ms 계산'):
                mes = message.content[10:]
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value = {int(mes) * 1000}  , inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content.startswith('준홍아 밴'): #해피야 밴 <@657876471750066186> 나쁜 짓 해떠여
                if message.author.guild_permissions.administrator:
                    author = message.content[9:27]
                    reason = message.content[29:] + f'\n\n밴 한 사람 : {message.author}'
                    await message.guild.get_member(int(author)).ban(reason=reason)
                    await message.channel.send(f"<@{author}> 님이 밴되었어요.\n사유 : {reason}")
                    return None
                else:
                    await message.channel.send('사용불가 커맨드입니다.')


            elif message.content.startswith('준홍아 공지'):
                if message.author.id in owner:
                    msg=message.content[7:]
                    embed=discord.Embed(
                        title=msg.split('and')[0],
                        description=msg.split('and')[1] + '\n\n[팀 SB 디스코드](http://discord.gg/UeWTsCg)\n[코어 엔터테인먼트](https://discord.gg/TeCpcBq)',
                        colour=discord.Colour.blue(),
                        timestamp=message.created_at
                    ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - 인증됨') .set_thumbnail(url=client.user.avatar_url)
                    for i in client.guilds:
                        arr=[0]
                        alla=False
                        flag=True
                        z=0
                        for j in i.channels:
                            arr.append(j.id)
                            z+=1
                            if "봇-공지" in j.name or "봇_공지" in j.name or "bot_announcement" in j.name or j.name in '『준홍봇ㆍ공지방』' or "봇공지" in j.name: 
                                if str(j.type)=='text':
                                    try:
                                        await j.send(embed=embed)
                                        alla=True

                                    except:
                                        pass
                                    break
                        if alla==False:
                            try:
                                chan=i.channels[1]
                            except:
                                pass
                            if str(chan.type)=='text':
                                try:
                                    await chan.send(embed=embed)
                                except:
                                    pass
                    await message.channel.send('완료')
                else:
                    await message.channel.send('권한없어')
                    return None

            elif message.content == '준홍아 뒤져':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="응 아니야", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 애교해봐':
                p = random.randint(1, 4)
                if p == 1:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value=("1 떠하기 1은 끼요미<퍼퍼퍼퍽ㄱ"), inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if p == 2:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value=("뭐요 안할거에요."), inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if p == 3:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value=("뀨?<ㅍ퍼퍼퍼ㅓ퍼퍼ㅓ"), inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if p == 4:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value=("쭌홍이까 때땅에서 까장 끼여워"), inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)


            elif message.content.startswith("준홍아 eval"):
                if message.author.id in owner:
                    a=message.content[9:]
                    
                    #if message.content in ['output','token', 'file=', 'os', 'logout', 'login', 'quit', 'exit', 'sys', 'shell', 'dir']:
                        #embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                        #embed.add_field(name="준홍봇 안내기능", value=f'{message.content} 그 명령어는 금지된 단어가 포함되어있습니다.', inline=True)
                        #embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                        #await message.channel.send(embed=embed)
                        #return None

                    try:
                        msg=await message.channel.send(embed=discord.Embed(color=0x85CFFF, title="evaling...",description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    evaling...
    ```"""))
                        aa=await eval(a)
                    except Exception as e:
                        await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval",description=f"""📥INPUT📥
                        
    ```py
    {a}          
    ```
    📤OUTPUT📤
    ```py
    {e}
    ```"""))
                        try:
                            aa = eval(a)
                        except Exception as e:
                            await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval",description=f"""📥INPUT📥
                        
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {e}
    ```"""))
                        else:
                            await msg.edit(embed=discord.Embed(color=0x85CFFF, title=f"eval",description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```""")) 
                    else:
                        await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval",description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```"""))
                else:
                    await message.channel.send("권한없음")

            elif message.content == '준홍아 승현':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="승현승현승현승현승현승현승현승현승현승현승현승현", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == "준홍아 stop":
                if message.author.id in owner:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 관리기능", value="정지중....", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                    os.system("pause")

            elif message.content == "준홍아 reboot":
                if message.author.id in owner:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 관리기능", value="재시작중....", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                    await client.close()
                    os.system("py V4_1.py")

            elif message.content == '준홍아 mswgen':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="mswgen바보", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 베인블':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="팀SB 관리자임 잘 모르겠지만 어쨌든 그런거임ㅋ",inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 LoL':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="Riot Games가 개발한 League of Legends",inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 현재시각':
                now = time.localtime()
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="%04d년%02d월%02d일 %02d시%02d분%02d초" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == '준홍아 업타임':
                current_time = time.time()
                difference = int(round(current_time - start_time))
                text = str(datetime.timedelta(seconds=difference))
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="업타임!", value=text)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content == 'test':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value=f"""```cpp
    
    cout
    ```""", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            elif message.content.startswith("준홍아 계산"):
                channel = message.channel
                math = message.content[7:]
                if math == "":
                    await message.channel.send('계산식를 입력해주세요')
                elif len(message.mentions) >= 1 or len(message.role_mentions) >= 1 or len(message.channel_mentions) >= 1:
                    await message.channel.send('계산식이 올바르지 않습니다..')
                else:
                    mathtext = ""
                    allowed = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "*", "/", "(", ")"]
                    for i in math:
                        if i in allowed:
                            mathtext += i
                        else:
                            mathtext += ""
                    try:
                        value = eval(mathtext)
                        embed=discord.Embed(
                            title=f'{mathtext}식의 결과',
                            description=f'{str(value)}',
                            colour=0x85CFFF
                        )
                        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                        await message.channel.send(embed=embed)
                    except:
                         await message.channel.send('계산식이 올바르지 않습니다..')

            elif message.content == '준홍아 애교해봐':
                p = random.randint(1,3)
                if p == 1:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="뀨?",inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if p == 2:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="1더하기 1은 뀌요미",inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if p == 3:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="쭌홍이까 때땅에서 까장 끼여워",inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)

            else:
                m = random.randint(1, 2)
                if m == 1:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name=":no_entry_sign: 명령어 안내 :no_entry_sign:", value="그게 무슨 명령어야?", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if m == 2:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name=":no_entry_sign: 명령어 안내 :no_entry_sign:", value=f'{message.content} 라는 명령어는 없어', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
    
    except Exception as ex:
        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        embed.add_field(name=":no_entry_sign: 오류!! ERROR!! :no_entry_sign:", value=f'에러 준홍봇에서 발생해요!\n에러에 대한 내용이 팀 SB에게 전송되었습니다!\n에러 내용 : {str(ex)}', inline=True)
        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        await client.get_channel(int(errorchannel)).send(f'guild : {message.channel.guild}({message.guild.id})\nch = {message.channel.name}({message.channel.id})\nauthor = {message.author}({message.author.id})\ncontent = {message.content}\nerror = {str(ex)}')

                                           
client.run(token)
