from pymongo import MongoClient
import discord, asyncio, pymongo, random, threading, time, ast, bs4, openpyxl, re, os, urllib, datetime, json, requests, smtplib, ctx, sys, configparser, platform, psutil, math, io, calendar,hgtk,psycopg2,webview
from PIL import Image
from itertools import cycle
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from shutil import copyfile
from json import loads
from captcha.image import ImageCaptcha

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


logchannel = 727388709485543485
errorchannel = 727388190549475400
owner = [447934468603379724, 340373909339635725,736075831226662984]
botjoinchannel = 695243394729115668
readylog = 727388158232232031
botleavelog = 697773473161936959
gunlog = 727388605516873790
Emergency = 734484279383293972
id = 503502157925056514
ban = []


start_time = time.time()

client = discord.Client()
game = discord.Game("준홍아 도움")    


#패기물



@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "📘":
        await reaction.message.channel.send(user.name + "님이 ?? 리액션을 하셨습니다.")

def korean_to_be_englished(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        ## 영어인 경우 구분해서 작성함. 
        if '가'<=w<='힣':
            ## 588개 마다 초성이 바뀜. 
            ch1 = (ord(w) - ord('가'))//588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(id)  
    await client.get_channel(readylog).send("준홍봇 전원 on")
    dagi = 8
    messages = ['준홍아 도움을 입력해 명령어 확인', f'{len(client.guilds)}개의 서버에 참여중', f'{len(client.users)}명의 유저들과 소통하는중', '안녕하세요', '문의는 junhong123a@naver.com 또는 준홍!good good#8922', '개인메세지는 `준홍아 갠챗`', '사용자 여러분 감사합니다!', f'이 메세지는 {dagi}초마다 바뀝니다.']
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(dagi)
       
@client.event
async def on_message(message):
    try:

        channel = message.channel
        if message.author.bot:                 
            return None

        if message.author.id in ban:
            embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
            embed.add_field(name="준홍봇 알림기능", value="당신은 밴(블랙리스트)되셨습니다." , inline=True)
            embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
            await channel.send(embed=embed)
            return None

        if message.content.startswith('준홍아'):
            embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
            embed.add_field(name="준홍봇 로그", value=f'guild : {message.channel.guild}({message.guild.id})\nch = {message.channel.name}({message.channel.id})\nauthor = {message.author}({message.author.id})\ncontent = {message.content}' , inline=True)
            embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
            await client.get_channel(int(logchannel)).send(embed=embed)

            if message.content == "준홍아 안녕":
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                await message.channel.send(f"<@{message.author.id}> 님 환영합니다!")
                embed.add_field(name="준홍봇 채팅기능", value="안녕하세요 준홍봇입니다. 준홍봇의 개발자는 준홍!good good#8922입니다.! 자세한 명령어는 `준홍아 도움 `을! \n그리고 왠만하면 봇DM에서 명령어는 사용안해주셨으면 합니다." , inline=True)
                embed.add_field(name="안내사항", value="준홍봇의 개발자 준홍은 봇 도우미로 활동하고 있습니다. 도움이 필요하신분은 준홍!good good#8922로 DM  주시기바랍니다.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == "준홍아 comjun04":
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="comjun04 흠" , inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith("준홍아 긴급"):
                if message.author.id in owner:
                    a = message.content[7:]
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 정지기능", value=f"긴급한 일이 일어나 봇을 중지시킵니다.사유가 팀SB에게 전달되었습니다.\n\n 사유: {a} ", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    os.system("pause")
                    await client.get_channel(int(Emergency)).send(f"긴급한 일이 일어나 봇을 중지시켰습니다. 사유 : {a}")

                    
            elif message.content  ==  '준홍아 핑':
                vld = client.latency * 1000
                if vld >= 0 and vld <= 199:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 정상 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

                elif vld >= 200 and vld <= 230:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 약간 느림 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

                elif vld >= 231 and vld <= 250:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 조금 느림 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')
                
                elif vld >= 251 and vld <= 333:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 매우 느림 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

                elif vld >= 334 and vld <= 100000:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 심각하게 느림 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

            elif message.content == "준홍아 블랙":
                b = message.content[7:]
                ban.append(b)
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 블랙기능", value="블랙추가 완료", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content  ==  '준홍아 수현':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="수현은 저랑 같이 봇 개발하는 개발자 입니다", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content  ==  '준홍아 호스팅':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="준홍봇은 헤로쿠(heroku) 호스팅으로 구동되고 있습니다.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 도움':
                try: 
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="보내는중..", value="<a:yes:690124935179272211>잠시 기다려 주세요", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    time.sleep(3)
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="안녕하세요! 명령어들 앞에는 `준홍아` 라는 칭호가 붙어요 ", value="도움말 시작", inline=True)
                    embed.add_field(name="준홍봇 도움말", value='기본명령어: 안녕, 핑, 수현, 도움, 죽어, say say형식 : 준홍아 say 할말, esay esay형식 : 준홍아 esay 할말, 네집, comjun04, 웹뷰', inline=True)
                    embed.add_field(name="기본명령어2:", value="찬반투표 찬반투표형식 : 준홍아 찬반투표 제목, 익명, 내정보, 내프사, 섭정보, 건의 건의 형식: 준홍아 건의 건의내용 ,심심해,준홍아,ㅎㅇ,Error", inline=True)
                    embed.add_field(name="기본명령어3", value="미쳤나, 빼에에엑, 주사위, 규카츠, RST, WCDMA, 짜장면, 냉면, 주소들, 삼해트, 개발코드, 닉네임, discord_api,정보,탕수육,감자칩, 실검, 호스팅", inline=True)
                    embed.add_field(name="기본명령어4", value="뭐해, star, Ms 계산 Ms계산 형식: 준홍아 Ms 계산 초 또는 m 초 또는 ms, 뒤져, 승현,mswgen,베인블,캡챠,LOL,현재시각,업타임,봇켜짐?,계산 계산형식:준홍아계산 계산식,애교해봐, 날씨 날씨형식: 준홍아 날씨 지역명", inline=True)
                    embed.add_field(name="관리자 명령어", value="청소 청소 형식 : 준홍아 청소 메세지 수 ,cmd cmd형식 : 준홍아 cmd 명령어(cmd),공지 공지형식 : 준홍아 공지 제목 and 내용,stop,reboot")
                    embed.add_field(name="관리자 명령어2", value="eval,pyeval,jseval,c++eval eval들 형식 : 준홍아 eval(py,js,c++) 명령어", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.author.send(embed=embed)
                except:
                   embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                   embed.add_field(name="ERROR", value="보내기에 실패하였습니다. DM이 닫혀있을수 있으니 설정을 확인해주세요.", inline=True)
                   embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                   await channel.send(embed=embed) 

            elif message.content  ==  '준홍아 죽어':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="그런말은 쓰면 나빠요", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 say'):
                try:
                    sms = message.content[8:]
                    await channel.send(sms)
                except:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 say 할말", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content.startswith('준홍아 esay'):
                try:
                    sms = message.content[9:]
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value=(sms), inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                except:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 esay 할말", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content.startswith('준홍아 갠챗'):
                try:
                    author = message.guild.get_member(int(message.content[7:25]))
                    msg = message.content[26:]
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 전송기능", value=msg, inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await author.send(embed=embed)
                    await message.delete()
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 전송기능", value=f'{author}님께 갠챗 전송이 완료되었습니다!', inline=True)
                    embed.set_footer(text=f"{message.author} 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                except:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 갠챗 유저ID 할말 (문제가 없는데 이메세지가 출력된다면 권한문제일수 있습니다.)", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content  ==  '준홍아 네집':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="준홍봇의 집은 준홍!good good&. 잊니 유튜브 채널 서버에요!!", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 찬반투표'):
                lern=message.content[9:]
                embed=discord.Embed(
                    title=str(lern),
                    description=f"{message.author.display_name}님의 찬반투표"
                )
                msg=await channel.send(embed=embed)
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
                    embed.set_footer(text=f'{message.author}, 인증됨', icon_url=message.author.avatar_url)
                    await channel.send(f'<@{message.author.id}>', embed=embed)

            elif message.content.startswith('준홍아 익명'):
                try:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 문의기능", value="익명으로 문의가 완료되었습니다!", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
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
                except:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 익명 할말", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)


            elif message.content.startswith('준홍아 내정보'):
                date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
                status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                    discord.Status.offline: ' <:status_offline:728527943831126036> 오프라인',
                    discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                    discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
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
                await channel.send(embed=embed)

            elif message.content == '준홍아 내프사':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 유저정보", value="유저의 프로필 사진입니다!", inline=True)
                embed.set_image(url=message.author.avatar_url)
                embed.set_footer(text=f"{message.author}, 인증됨 ", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith("준홍아 날씨"):
                location = message.content[7:]
                NowTemp = ""
                Finallocation = location + '날씨'
                CheckDust = []

                url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + Finallocation 
                hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
                req = requests.get(url, headers=hdr) 
                html = req.text 
                soup = BeautifulSoup(html, 'html.parser')

                NowTemp = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span', {'class' : 'tempmark'}).text[2:]
                WeatherCast = soup.find('p', {'class' : 'cast_txt'}).text
                TodayMorningTemp = soup.find('span', {'class' : 'min'}).text 
                TodayAfternoonTemp = soup.find('span', {'class' : 'max'}).text 
                TodayFeelTemp = soup.find('span', {'class' : 'sensible'}).text[5:]
                TodayUV = soup.find('span', {'class' : 'indicator'}).text[4:-2] + " " + soup.find('span', {'class' : 'indicator'}).text[-2:]
                CheckDust1 = soup.find('div', {'class': 'sub_info'}) 
                CheckDust2 = CheckDust1.find('div', {'class': 'detail_box'})
                for i in CheckDust2.select('dd'):
                    CheckDust.append(i.text)
                FineDust = CheckDust[0][:-2] + " " + CheckDust[0][-2:] 
                UltraFineDust = CheckDust[1][:-2] + " " + CheckDust[1][-2:] 
                Ozon = CheckDust[2][:-2] + " " + CheckDust[2][-2:]
            
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at,  title=f'{location} 날씨')
                embed.add_field(name="=========================", value="사용해 주셔서 감사합니다!", inline=True)
                embed.add_field(name="정보", value=f'{location} 날씨 정보입니다.', inline=False)
                embed.add_field(name="현재온도", value=f'{NowTemp}', inline=True)
                embed.add_field(name="체감온도", value=f'{TodayFeelTemp}', inline=True)
                embed.add_field(name="오전/오후 온도", value=f'{TodayMorningTemp} / {TodayAfternoonTemp}', inline=True)
                embed.add_field(name="현재날씨정보", value=f'{WeatherCast}', inline=True)
                embed.add_field(name="현재 자외선 지수", value=f'{TodayUV}', inline=True)
                embed.add_field(name="현재 미세먼지 농도", value=f'{FineDust}', inline=True)
                embed.add_field(name="현재 초미세먼지 농도", value=f'{UltraFineDust}', inline=True)
                embed.add_field(name="현재 오존 지수", value=f'{Ozon}', inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨 ", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == "준홍아 실검":
                embed=discord.Embed(title=f"네이버 실시간 검색 정보", colour=0x85CFFF, timestamp=datetime.datetime.utcnow())
                for r in requests.get('https://www.naver.com/srchrank?frm=main').json().get("data")[:10]:
                    embed.add_field(name=f"**{r.get('rank')}위**", value=f"[{r.get('keyword')}](https://search.naver.com/search.naver?where=nexearch&query={r.get('keyword').replace(' ', '+')})", inline=False)
                embed.set_footer(text=f"{message.author}, 인증됨, 도움 : OWO#1996", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)
                

            elif message.content == '준홍아 섭정보' or message.content == "준홍아 서버정보":
                rnrrk = message.guild.region
                print(message.guild.region)
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"서버 정보 - {message.guild.name}")
                embed.set_thumbnail(url=message.guild.icon_url)
                embed.add_field(name="서버 기본정보", value="서버의 기본 정보입니다.", inline=False)
                embed.add_field(name="서버 이름", value=message.guild.name, inline=True)
                embed.add_field(name="서버 ID", value=message.guild.id, inline=True)
                embed.add_field(name="서버 위치", value=rnrrk, inline=True)
                embed.add_field(name="서버 주인", value=f'<@{message.guild.owner.id}>', inline=True)
                embed.add_field(name="서버 주인 ID", value=message.guild.owner.id, inline=True)
                embed.add_field(name="서버 채널 수", value=f'전체 채널: {len(message.guild.channels)}개 (채팅채널 : {len(message.guild.text_channels)}개 | 음성채널 : {len(message.guild.voice_channels)}개 | 카테고리 : {len(message.guild.categories)}개)', inline=True)
                embed.add_field(name="서버 유저정보", value="서버의 유저 정보입니다.", inline=False)
                embed.add_field(name="서버 멤버 수", value=f'{len(message.guild.members)}명 (봇 : {len(list(filter(lambda x: x.bot, message.guild.members)))}명 | 유저 : {len(list(filter(lambda x: not x.bot, message.guild.members)))}명)', inline=True)
                embed.add_field(name="서버 부스트정보", value="서버의 부스트 정보입니다.", inline=False)
                embed.add_field(name="서버 부스트 레벨", value=f'<:boost:707784277307293747> {message.guild.premium_tier}레벨', inline=True)
                embed.add_field(name="서버 부스트 횟수", value=f'<:boost:707784277307293747> {message.guild.premium_subscription_count}번', inline=True)
                embed.add_field(name="서버 잠수채널/시스템채널 정보", value="서버의 잠수채널/시스템채널 정보입니다.", inline=False)
                if message.guild.afk_channel != None:
                    embed.add_field(name = f'잠수 채널', value = f'<a:yes:707786803414958100> 잠수 채널이 있습니다.\n{message.guild.afk_channel.name} (타이머: {message.guild.afk_timeout})', inline = True)
                else:
                    embed.add_field(name="잠수 채널", value="<a:no:707786855143309370> 잠수 채널이 없습니다.")
                if message.guild.system_channel != None:
                    embed.add_field(name = f'시스템 채널', value = f'<a:yes:707786803414958100> 시스템 채널이 있습니다.\n<#{message.guild.system_channel.id}>', inline = True)
                else:
                    embed.add_field(name="잠수 채널", value="<a:no:707786855143309370> 시스템 채널이 없습니다.")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 건의'):
                try:
                    msg = str(message.content[7:])
                    if(msg == None):
                        await channel.send("사용방법: 준홍아 건의 할말")
                    else:
                        await channel.send("건의가 완료되었습니다!")
                        await client.get_channel(int(gunlog)).send(f'<@447934468603379724>')
                        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                        embed.add_field(name="준홍봇 건의", value=f'{message.author}({message.author.id})님의 건의 : {msg}', inline=True)
                        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                        await client.get_channel(int(gunlog)).send(embed=embed)
                except:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 건의 할말", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content  ==  '준홍아 심심해':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="심심할땐 역시 게임이죠!", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content  ==  '준홍아':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="안녕하세요!", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content  ==  '준홍아 ㅎㅇ':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="안녕하세요", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content  ==  '준홍아 Error':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="Error가 발생했습니다.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)
                        
            elif message.content  ==  '준홍아 미쳤나':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="아니요 도 쳤어요.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content  ==  '준홍아 타자':
                fltmxm = random.randint(0,2)
                xkwk=["몰라ㅇ", "test", "안녕하세요"]
                cncnf=xkwk[fltmxm]
                await message.channel.send(f'{cncnf}')
                checktime = time.time()
                def check(m):
                    return m.content == f'{cncnf}' and m.channel == channel #해볼까
                
       
                msg = await client.wait_for('message', check=check)
                end = time.time()
                et = end - checktime                     # 실제로 걸린 시간을 계산
                et = format(et, ".2f")
                al = len(hgtk.text.decompose(f'{cncnf}')) / float(et) * 60
                await channel.send(f'<@{message.author.id}>, {et}초, {round(al,2)}타')

            elif message.content == '준홍아 빼에에엑':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="뻬에에에에에ㅔㄱ", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)
            
            elif message.content == '준홍아 주사위':
                dice = random.randint(1, 6)
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value=(dice), inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)
            
            elif message.content == '준홍아 규카츠':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA0MDlfOTgg%2FMDAxNTIzMjQ4NTQxOTgy.27rWawoPnQujw6HS4nPxcYjsbdZYnq-Ml3w0Q9DA3ggg.ECeoJu1W2ZiaWM8GvnPKGUylujeSjddKzkVMHZ1MuSYg.JPEG.creamy0080%2F12.%25B4%25EB%25C0%25FC%25C1%25DF%25BE%25D3%25BF%25AA%25B8%25C0%25C1%25FDDSC03358..jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)
            
            elif message.content == '준홍아 RST':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="아두이노에서 RESET을 담당하는 포트", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 WCDMA':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="와이드밴드 코드분할 다중접속기술, wideband code division multiple access", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 짜장면':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="http://post.phinf.naver.net/MjAxNzEyMDVfMTgx/MDAxNTEyNDUzODM1Nzgz.oLCRrLmG048QINV4T7flJ1n5whWnMgXe2FPzjD8wvMog.1fVLRKcFZlnTg3DYFO8wrGnW9wZyZpx7Yd8hkGG3RTsg.JPEG/IIh6-J6mXMeGwnXBKX2yJP5ooR_0.jpg")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 냉면':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="http://post.phinf.naver.net/MjAxODA2MDdfMzUg/MDAxNTI4MzUyNjUzMDE1.ZA0IG7V1Ghd2c1FAp1JPvH__g8kKncVHOOYj8wkEFn4g.xGGLSjvb4a4Pqu35ghIEh7WhCwRzxm80BWxNo9q1U3Ig.JPEG/I-5vjeJnAa7azL8tI3ihsiYYU6oQ.jpg")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 주소들':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="서포트 서버 : https://discord.gg/jkWNWgG ", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)
            
            elif message.content == '준홍아 삼해트':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="삼해트 바보 멍청이", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)
            
            elif message.content == '준홍아 개발코드':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value='파이썬으로 개발됬어요!', inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 닉네임':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value=f"{message.author.display_name} 입니다.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)


            elif message.content == '준홍아 discord_api':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value='절 많이 도와주는 팀원입니다.', inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 청소'):
                if message.author.id in owner:
                #if message.author.guild_permissions.administrator:
                    varrr=message.content.split(' ')
                    await message.channel.purge(limit=int(varrr[2])+1)
                    msg=await message.channel.send(embed=discord.Embed(title=f'메시지 {str(int(varrr[2]))}개 삭제 완료!', descirption='응용 기능',timestamp=message.created_at, colour=discord.Colour.blue()).set_footer(icon_url=message.author.avatar_url, text=f'{str(message.author)}, 인증됨'))
                    await asyncio.sleep(3)
                    await msg.delete()
                else:
                    await channel.send("뭐하시는거죠")

            

            elif message.content.startswith("준홍아 cmd"):
                if message.author.id in owner:
                    try:
                        a = message.content[8:]
                    except:
                        await message.channel.send("내용을 입력해주세요!")
                        return
                    proc = await asyncio.create_subprocess_shell(a, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
                    dd, _  = await proc.communicate()
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="cmd", value=f"{dd.decode('cp949')}", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

                
            elif message.content.startswith('준홍아 정보'):
                if str(message.content[7:]) == '':
                    user = message.author
                    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                    status_dict: dict = {discord.Status.online: '<:status_online:707783912121696256> 온라인',
                        discord.Status.offline: '<:status_offline:707783990953771069> 오프라인',
                        discord.Status.idle: "<:status_idle:707783934095917106> 자리비움",
                        discord.Status.do_not_disturb: "<:status_dnd:707783959634903110> 방해금지"} # 님 어떻게 됬음??/ 고쳣는데 왜 적용이 안됨..; 저장 Autosave no? 왔? 그게 뭐꼬 
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
                    await channel.send(embed=embed)
                else:
                    try:
                        user = message.guild.get_member(int(message.content.split('<@!')[1].split('>')[0]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
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
                            await channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
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
                            await channel.send(embed=embed)
                    except:
                        user = message.guild.get_member(int(message.content.split('<@')[1].split('>')[0]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
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
                            await channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
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
                            await channel.send(embed=embed)

            elif message.content == '준홍아 탕수육':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20130412_259%2Froyalrate7_1365760080337VvTgW_JPEG%2FDSCN7945.jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 감자칩':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzEyMTJfMjA4%2FMDAxNTEzMDc4MjgwMjE5.B5xVKAl3CNo8jaYf0trsO8Wr_8XfJJRjmwn8rO6VNM0g.I5dfl1H7vyDdeK0C0xAx7cNaRyIkEYvzed3gJRhxTGgg.JPEG.changuk1225%2F%25BD%25BA%25C6%25E4%25C0%25CE_%25C6%25E4%25C0%25CE%25C6%25AE%25C5%25EB_%25B0%25A8%25C0%25DA%25C4%25A8_%25BA%25B8%25B4%25D2%25B6%25F3%25B0%25A8%25C0%25DA%25C4%25A8_5.jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 뭐해':
                a=random.randint(1,2)
                if a == 1:
                     embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                     embed.add_field(name="준홍봇 채팅기능", value="나? 수현이랑 놀거나  준홍 괴롭히지 ㅎㅎㅎㅎ", inline=True)
                     embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                     await channel.send(embed=embed)
                if a == 2:
                     embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                     embed.add_field(name="준홍봇 채팅기능", value="준홍에게 개발 이라는 고문을 받..죄송합니다. 사실 노는중임ㅋㅋ", inline=True)
                     embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                     await channel.send(embed=embed)

            elif message.content == '준홍아 star':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="star 잘생김", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 Ms 계산'):
                mes = message.content[10:11]
                ty = message.content[13:]

                if mes == "초":
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value=f'{ty} * 1000', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

                if mes == "m":
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value=f'{ty} / 1000', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content.startswith('준홍아 밴'): #해피야 밴 <@657876471750066186> 나쁜 짓 해떠여
                if message.author.guild_permissions.administrator:
                    author = message.content[9:27]
                    reason = message.content[29:] + f'\n\n밴 한 사람 : {message.author}'
                    await message.guild.get_member(int(author)).ban(reason=reason)
                    await message.channel.send(f"<@{author}> 님이 밴되었어요.\n사유 : {reason}")
                    return None
                else:
                    await channel.send("권한없음")


            elif message.content.startswith('>>공지'):
                if message.author.id in owner:
                    msg=message.content[7:]
                    embed=discord.Embed(
                        title=msg.split('and')[0],
                        description=msg.split('and')[1] + '\n\n이 체널에 공지가 오는것이 싫다면 `봇-공지` 채널을 만들어주세요! \n\n[팀 SB 디스코드](http://discord.gg/UeWTsCg)\n[코어 엔터테인먼트](https://discord.gg/TeCpcBq)',
                        colour=discord.Colour.blue(),
                        timestamp=message.created_at
                    ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - 인증됨') .set_thumbnail(url=client.user.avatar_url)
                    for i in client.guilds:
                        arr=[0]
                        alla=False
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
                    await channel.send("완료")
                else:
                    await channel.send("NO 권한")
                    return None

            elif message.content == '준홍아 뒤져':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="그런말은 나빠요..", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)


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
    ```
    {a}
    ```
    📤OUTPUT📤
    ```py
    evaling...
    ```"""))
                        aa=await eval(a)
                    except Exception as e:
                        await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval",description=f"""📥INPUT📥
                        
    ```
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
                        
    ```
    {a}
    ```
    📤OUTPUT📤
    ```py
    {e}
    ```"""))
                        else:
                            await msg.edit(embed=discord.Embed(color=0x85CFFF, title=f"eval",description=f"""📥INPUT📥
    ```
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```""")) 
                    else:
                        await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval",description=f"""📥INPUT📥
    ```
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```"""))
                else:
                    await channel.send("권한없음")
  
            elif message.content.startswith("준홍아 pyeval"):
                if message.author.id in owner:
                    a=message.content[11:]
                    
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
                    await channel.send("권한없음")
            
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
                    await channel.send(embed=embed)
                    os.system("pause") 

            elif message.content == "준홍아 reboot":
                if message.author.id in owner:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 관리기능", value="재시작중....", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    await client.close()
                    os.system("py V4_1.py")

            elif message.content == '준홍아 mswgen':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="mswgen바보", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 베인블':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="팀SB 관리자임 잘 모르겠지만 어쨌든 그런거임ㅋ",inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 캡챠'):
                Image_captcha = ImageCaptcha()
                msg = ""
                a = ""
                for i in range(6):
                    a += str(random.randint(0, 9))

                name = str(message.author.id) + ".png"
                Image_captcha.write(a, name)
                
                await channel.send(file=discord.File(name))
                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel

                try:
                    msg = await client.wait_for("message", timeout=10, check=check)
                except:
                    await message.channel.send("시간초과입니다.")
                    return
 
                if msg.content == a:
                    await message.channel.send("정답입니다!")
                else:
                    await message.channel.send("오답입니다.")

            elif message.content.startswith("준홍아 웹뷰"):
                aa = message.content[7:]
                namd = str(aa)
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title="준홍봇 웹뷰기능")
                embed.set_image(url=namd)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)


            elif message.content == '준홍아 LoL':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="Riot Games가 개발한 League of Legends",inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            #elif message.content == '준홍아 현재시각':
                #now = time.localtime()
                #embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                #embed.add_field(name="준홍봇 채팅기능", value="%02d시%02d분%02d초" % ((now.hour)+9, (now.now.min), (now.tm_sec))
                #embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                #await channel.send(embed=embed)

            elif message.content == '준홍아 업타임':
                current_time = time.time()
                difference = int(round(current_time - start_time))
                text = str(datetime.timedelta(seconds=difference))
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="업타임!", value=text, inline=True)
                embed.set_thumbnail(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzAzMThfMjA2%2FMDAxNDg5ODAyMjg2NTQ1.vwHEuHuFRL0QeQGnxz9k6cVM7_Hm0kDNHGABDIyq1Wcg.oVIF0Bn7HEueDmc9sa_GT9zVMkMji5h0SNlUICcXNFgg.GIF.nico1691%2F1.gif&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 봇켜짐?':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="ㅇㅇ 켜짐", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 사진'):
                pic = message.content.split(' ')[2]
                await channel.send(file=discord.File(pic))

            elif message.content.startswith("준홍아 계산"):
                channel = message.channel
                math = message.content[7:]
                if math == "":
                    await message.channel.send('계산식를 입력해주세요')
                elif len(message.mentions) >= 1 or len(message.role_mentions) >= 1 or len(message.channel_mentions) >= 1:
                    await message.channel.send('계산식이 올바르지 않습니다..')
                else:
                    mathtext = ""
                    allowed = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "*","**","x", "X", "^", "/", "(", ")"]
                    for i in math:
                        if i in allowed:
                            mathtext += i
                        else:
                            mathtext += ""
                    try:
                        value = eval(mathtext)
                        embed=discord.Embed(
                            title=f'{mathtext} 식의 결과',
                            description=f'{str(value)}',
                            colour=0x85CFFF
                        )
                        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                        await channel.send(embed=embed)
                    except:
                        await channel.send("계산식이 올바르지 않습니다..")

            elif message.content == '준홍아 애교해봐':
                p = random.randint(1,3)
                if p == 1:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="하고싶지 않습니다",inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                if p == 2:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="1더하기 1은 기요미",inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                if p == 3:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="낙으로 보냈습니다.",inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            else:
                m = random.randint(1, 2)
                if m == 1:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name=":no_entry_sign: 명령어 안내 :no_entry_sign:", value="그게 무슨 명령어야?", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                if m == 2:
                    embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name=":no_entry_sign: 명령어 안내 :no_entry_sign:", value=f'{message.content} 이/라는 명령어는 없어', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
    
    except Exception as ex:
        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        embed.add_field(name=":no_entry_sign: 오류!! ERROR!! :no_entry_sign:", value=f'에러 준홍봇에서 발생해요!\n에러에 대한 내용이 팀 SB에게 전송되었습니다!\n에러 내용 : {str(ex)} 사용방법이 궁금하시다면 `준홍아 도움`', inline=True)
        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
        await channel.send(embed=embed)
        await client.get_channel(int(errorchannel)).send(f'guild : {message.channel.guild}({message.guild.id})\nch = {message.channel.name}({message.channel.id})\nauthor = {message.author}({message.author.id})\ncontent = {message.content}\nerror = {str(ex)}')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
