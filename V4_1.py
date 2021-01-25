import aiohttp, discord, asyncio, random, time, os, datetime, requests, math, hgtk
from bs4 import BeautifulSoup

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

logchannel = 762179726927986718
errorchannel = 762179910004506634
owner = [447934468603379724]
botjoinchannel = 704252617680748618
readylog = 762180021422391336
botleavelog = 704252617680748618
gunlog = 762179801712558080
sulog = 762179801712558080
Emergency = 762179874772484106
id = 503502157925056514
ban = []

start_time = time.time()
intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

def log_info(channel, user, message):
    Ftime = time.strftime('%Y-%m-%d %p %I:%M:%S', time.localtime(time.time()))
    print("[시간: " + str(Ftime) + ",채널: " + str(channel) + ",유저: " + str(user) + "]: " + str(message))
    log = open("log.txt","a")
    log.write("[시간: " + str(Ftime) + ",채널: " + str(channel) + ",유저: " + str(user) + "]: " + str(message) + "\n")
    log.close()

async def get_text_from_url(url):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url, headers={'user-agent': 'Mozilla/5.0'}) as res:
            text = await res.text()
    text = BeautifulSoup(text, 'html.parser').text


@client.event
async def on_ready():
    log_info('Local', 'Local', "로그인 승인")
    log_info('Local', "Local", client.user.name)
    log_info("Local", "Local", id)
    await client.get_channel(readylog).send("준홍봇 전원 on")
    dagi = 8
    messages = ['준홍아 도움을 입력해 명령어 확인', f'{len(client.guilds)}개의 서버에 참여중', f'{len(client.users)}명의 유저들과 소통하는중', '안녕하세요', '문의는 junhong123a@naver.com 또는 준홍!good good#8922', '개인메세지는 `준홍아 갠챗`', '사용자 여러분 감사합니다!',f'이 메세지는 {dagi}초마다 바뀝니다.']
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(dagi)



@client.event
async def on_message(message):
    try:
        channel = message.channel
        if message.author.bot:
            return

        if message.content.startswith('준홍아'):
            log_info(message.channel, message.author, message.content)
            embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
            embed.add_field(name="준홍봇 로그",value=f'guild : {message.channel.guild}({message.guild.id})\nch = {message.channel.name}({message.channel.id})\nauthor = {message.author}({message.author.id})\ncontent = {message.content}', inline=True)
            embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
            await client.get_channel(int(logchannel)).send(embed=embed)

            if message.content == "준홍아 안녕":
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                await message.channel.send(f"<@{message.author.id}> 님 환영합니다!")
                embed.add_field(name="준홍봇 채팅기능", value="안녕하세요 준홍봇입니다. 준홍봇의 개발자는 준홍!good good#8922입니다.! 자세한 명령어는 `준홍아 도움 `을! \n그리고 왠만하면 봇DM에서 명령어는 사용안해주셨으면 합니다.",inline=True)
                embed.add_field(name="안내사항",value="준홍봇의 개발자 준홍은 봇 도우미로 활동하고 있습니다. 도움이 필요하신분은 준홍!good good#8922로 DM  주시기바랍니다.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == "준홍아":
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 인사기능", value="안녕하세요! 준홍아 안녕을 입력해보세요~^^7", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith("준홍아 긴급"):
                if message.author.id in owner:
                    a = message.content[7:]
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 정지기능", value=f"긴급한 일이 일어나 봇을 중지시킵니다.사유가 팀SB에게 전달되었습니다.\n\n 사유: {a} ", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    await client.get_channel(int(Emergency)).send(f"긴급한 일이 일어나 봇을 중지시켰습니다. 사유 : {a}")
                    os.system("pause")

            elif message.content == '준홍아 핑':
                vld = client.latency * 1000
                if vld >= 0 and vld <= 199:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 정상 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

                elif  vld >= 200 and vld <= 230:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 약간 느림 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

                elif vld >= 231 and vld <= 250:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 조금 느림 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

                elif vld >= 251 and vld <= 333:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 매우 느림 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

                elif vld >= 334 and vld <= 100000:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(vld)}ms, 상태: 심각하게 느림 입니다!', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    print(f'ping is {round(vld)}ms')

            elif message.content == '준홍아 수현':
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="수현은 저랑 같이 봇 개발하는 개발자 입니다", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == "준홍아 하위":
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="안녕하신가, 용사여", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == "준홍아 도움":
                try:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="도움말 전송중........", value="도움말을 전송중입니다. 잠시만 기다려 주십시오.", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    time.sleep(3)
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title="준홍봇 도움말", description="모든 명령어 앞엔 `준홍아` 라는 접두사가 붙습니다.")
                    embed.add_field(name="기본명령어1", value="안녕, 핑, 도움, 멜론차트, 내정보, 내프사, 실검, 섭정보(서버정보), 타자, 주사위, 규카트, 짜장면, 냉면, 타자", inline=True)
                    embed.add_field(name="기본명령어2", value="개발코드, 닉네임, 탕수육, 감자칩, 뭐해, 현재시각, 업타임, 봇켜짐, 에교해봐", inline=True)
                    embed.add_field(name="서식필요명령어", value="say, esay, 갠챗, 찬반투표, 익명, 날씨, 건의, 정보, 계산, 단어학습", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.author.send(embed=embed)
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title="서식필요명령어 도움말")
                    embed.add_field(name="간단한 서식 명령어1", value="say, esay 사용법 : 준홍아 say(esay) 할말, 찬반투표 사용법 : 준홍아 찬반투표 투표의 이름, 익명 사용법 : 준홍아 익명 할말", inline=False)
                    embed.add_field(name="간단한 서식 명령어2", value="날씨 사용법 : 준홍아 날씨 지역명, 건의 사용법 : 준홍아 건의 건의 할 내용, 단어학습 사용법 : 준홍아 단어학습 입력할 단어 답으로 나올 단어", inline=False)
                    embed.add_field(name="복잡한 서식 명령어2", value="갠챗 사용법 : 준홍아 갠챗 갠챗을 받을 유저 ID 할말, 정보 사용법 : 준홍아 정보 유저ID 또는 맨션(@mention)", inline=False)
                    embed.add_field(name="복잡한 서식 명령어2", value="계산 사용법 : 준홍아 계산 계산식", inline=False)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await message.author.send(embed=embed)
                except:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="도움말 전송실패!", value="도움말 전송을 실패하였습니다. DM을 열어주세요.", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content.startswith('준홍아 say'):
                    try:
                        sms = message.content[8:1023]
                        await channel.send(sms)
                    except:
                        embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                        embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 say 할말", inline=True)
                        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                        await channel.send(embed=embed)

            elif message.content.startswith('준홍아 esay'):
                try:
                    sms = message.content[9:1023]
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value=(sms), inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                except:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 esay 할말", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content.startswith('준홍아 갠챗'):
                try:
                    author = message.guild.get_member(int(message.content[7:25]))
                    msg = message.content[26:]
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 전송기능", value=msg, inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await author.send(embed=embed)
                    await message.delete()
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 전송기능", value=f'{author}님께 갠챗 전송이 완료되었습니다!', inline=True)
                    embed.set_footer(text=f"{message.author} 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                except:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 갠챗 유저ID 할말 (문제가 없는데 이메세지가 출력된다면 권한문제일수 있습니다.)", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content.startswith('준홍아 찬반투표'):
                lern = message.content[9:]
                embed = discord.Embed(
                    title=str(lern),
                    description=f"{message.author.display_name}님의 찬반투표"
                )
                msg = await channel.send(embed=embed)
                await msg.add_reaction('👍')
                await msg.add_reaction('👎')

            elif message.content == '준홍아 멜론차트':
                    RANK = 10
                    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
                    req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
                    html = req.text
                    parse = BeautifulSoup(html, 'html.parser')
                    titles = parse.find_all("div", {"class": "ellipsis rank01"})
                    songs = parse.find_all("div", {"class": "ellipsis rank02"})
                    titles = get_text_from_url("ttps://www.melon.com/chart/index.htm")
                    title = []
                    song = []
                    embed = discord.Embed(
                        title="멜론차트 상위권(1~10위)\n차트 출처 : kakao(melon)\n",
                        colour=0x85CFFF, timestamp=message.created_at
                    )
                    for t in titles:
                        title.append(t.find('a').text)
                    for s in songs:
                        song.append(s.find('span', {"class": "checkEllipsis"}).text)
                    for i in range(RANK):
                        embed.add_field(name='%3d위' % (i + 1), value='%s - %s' % (title[i], song[i]), inline=False)
                    embed.set_footer(text=f'{message.author}, 인증됨', icon_url=message.author.avatar_url)
                    await channel.send(f'<@{message.author.id}>', embed=embed)

            elif message.content.startswith('준홍아 익명'):
                try:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 문의기능", value="익명으로 문의가 완료되었습니다!", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    mes = message.content
                    index = mes[4:]
                    embedadmin = discord.Embed(title=index, description="보낸사람 <@%s>" % (str(message.author.id)))
                    channelid = 762180378844463155  # 글이 작성되는 채널
                    adminch = 762180378844463155  # 보낸사람이 누군지 확인할수있는 채널id
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="익명메세지", value=(index), inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await client.get_channel(channelid).send(embed=embed)
                    await client.get_channel(adminch).send(embed=embedadmin)
                except:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 익명 할말", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)


            elif message.content.startswith('준홍아 내정보'):
                date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
                status_dict: dict = {discord.Status.online: '<:status_online:754547779845750864> 온라인',
                    discord.Status.offline: '<:status_offline:754547779606544394> 오프라인',
                    discord.Status.idle: "<:status_idle:754547779174531114> 자리비움",
                    discord.Status.do_not_disturb: "<:status_dnd:754547779048570970> 방해금지"}
                user_status = status_dict[message.author.status]
                roles = [role for role in message.author.roles]
                embed = discord.Embed(colour=message.author.color, timestamp=message.created_at)
                embed.set_author(name=f"유저정보 - {message.author}")
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.set_footer(text=f"{message.author},인증됨 ", icon_url=message.author.avatar_url)
                embed.add_field(name="아이디", value=f"{message.author.id}", inline=False)
                embed.add_field(name="닉네임", value=f"{message.author.display_name}", inline=False)
                embed.add_field(name="가입일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일",inline=False)
                embed.add_field(name=f"가진 역할들({len(roles) - 1}개)",value=f" ".join([role.mention for role in roles][1:]), inline=False)
                embed.add_field(name="가장 높은 역할", value=f"{message.author.top_role.mention}", inline=False)
                embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                embed.set_footer(text=f"{message.author}, 인증됨 ", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 내프사':
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
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
                hdr = {'User-Agent': (
                    'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')}
                req = requests.get(url, headers=hdr)
                html = req.text
                soup = BeautifulSoup(html, 'html.parser')

                NowTemp = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span',{'class': 'tempmark'}).text[2:]
                WeatherCast = soup.find('p', {'class': 'cast_txt'}).text
                TodayMorningTemp = soup.find('span', {'class': 'min'}).text
                TodayAfternoonTemp = soup.find('span', {'class': 'max'}).text
                TodayFeelTemp = soup.find('span', {'class': 'sensible'}).text[5:]
                TodayUV = soup.find('span', {'class': 'indicator'}).text[4:-2] + " " + soup.find('span', {'class': 'indicator'}).text[-2:]
                CheckDust1 = soup.find('div', {'class': 'sub_info'})
                CheckDust2 = CheckDust1.find('div', {'class': 'detail_box'})
                for i in CheckDust2.select('dd'):
                    CheckDust.append(i.text)
                FineDust = CheckDust[0][:-2] + " " + CheckDust[0][-2:]
                UltraFineDust = CheckDust[1][:-2] + " " + CheckDust[1][-2:]
                Ozon = CheckDust[2][:-2] + " " + CheckDust[2][-2:]

                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f'{location} 날씨')
                embed.add_field(name="=========================", value=f"{Finallocation} 정보입니다", inline=True)
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
                embed = discord.Embed(title=f"네이버 실시간 검색 정보", colour=0x85CFFF, timestamp=datetime.datetime.utcnow())
                for r in requests.get('https://www.naver.com/srchrank?frm=main').json().get("data")[:10]:
                    embed.add_field(name=f"**{r.get('rank')}위**",value=f"[{r.get('keyword')}](https://search.naver.com/search.naver?where=nexearch&query={r.get('keyword').replace(' ', '+')})",inline=False)
                embed.set_footer(text=f"{message.author}, 인증됨, 도움 : OWO#1996", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 섭정보' or message.content == "준홍아 서버정보":
                rnrrk = message.guild.region
                print(message.guild.region)
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at,title=f"서버 정보 - {message.guild.name}")
                embed.set_thumbnail(url=message.guild.icon_url)
                embed.add_field(name="서버 기본정보", value="서버의 기본 정보입니다.", inline=False)
                embed.add_field(name="서버 이름", value=message.guild.name, inline=True)
                embed.add_field(name="서버 ID", value=message.guild.id, inline=True)
                embed.add_field(name="서버 위치", value=rnrrk, inline=True)
                embed.add_field(name="서버 주인", value=f'<@{message.guild.owner.id}>', inline=True)
                embed.add_field(name="서버 주인 ID", value=message.guild.owner.id, inline=True)
                embed.add_field(name="서버 채널 수",value=f'전체 채널: {len(message.guild.channels)}개 (채팅채널 : {len(message.guild.text_channels)}개 | 음성채널 : {len(message.guild.voice_channels)}개 | 카테고리 : {len(message.guild.categories)}개)',inline=True)
                embed.add_field(name="서버 유저정보", value="서버의 유저 정보입니다.", inline=False)
                embed.add_field(name="서버 멤버 수",value=f'{len(message.guild.members)}명 (봇 : {len(list(filter(lambda x: x.bot, message.guild.members)))}명 | 유저 : {len(list(filter(lambda x: not x.bot, message.guild.members)))}명)',inline=True)
                embed.add_field(name="서버 부스트정보", value="서버의 부스트 정보입니다.", inline=False)
                embed.add_field(name="서버 부스트 레벨", value=f'<:boost:707784277307293747> {message.guild.premium_tier}레벨',inline=True)
                embed.add_field(name="서버 부스트 횟수", value=f'<:boost:707784277307293747> {message.guild.premium_subscription_count}번', inline=True)
                embed.add_field(name="서버 잠수채널/시스템채널 정보", value="서버의 잠수채널/시스템채널 정보입니다.", inline=False)
                if message.guild.afk_channel != None:
                    embed.add_field(name=f'잠수 채널',value=f'<a:yes:707786803414958100> 잠수 채널이 있습니다.\n{message.guild.afk_channel.name} (타이머: {message.guild.afk_timeout})',inline=True)
                else:
                    embed.add_field(name="잠수 채널", value="<a:no:707786855143309370> 잠수 채널이 없습니다.")
                if message.guild.system_channel != None:
                    embed.add_field(name=f'시스템 채널',value=f'<a:yes:707786803414958100> 시스템 채널이 있습니다.\n<#{message.guild.system_channel.id}>',inline=True)
                else:
                    embed.add_field(name="잠수 채널", value="<a:no:707786855143309370> 시스템 채널이 없습니다.")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 건의'):
                try:
                    msg = str(message.content[7:])
                    if (msg == None):
                        await channel.send("사용방법: 준홍아 건의 할말")
                    else:
                        await channel.send("건의가 완료되었습니다!")
                        await client.get_channel(int(gunlog)).send(f'<@447934468603379724>')
                        embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                        embed.add_field(name="준홍봇 건의", value=f'{message.author}({message.author.id})님의 건의 : {msg}',inline=True)
                        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                        await client.get_channel(int(gunlog)).send(embed=embed)
                except:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="사용방법: 준홍아 건의 할말", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.authokr.avatar_url)
                    await channel.send(embed=embed)

            elif message.content == '준홍아 타자':
                fltmxm = random.randint(0, 2)
                xkwk = ["몰라ㅇ", "test", "안녕하세요"]
                cncnf = xkwk[fltmxm]
                await message.channel.send(f'{cncnf}')
                checktime = time.time()

                def check(m):
                    return m.content == f'{cncnf}' and m.channel == channel  # 해볼까

                msg = await client.wait_for('message', check=check)
                end = time.time()
                et = end - checktime  # 실제로 걸린 시간을 계산
                et = format(et, ".2f")
                al = len(hgtk.text.decompose(f'{cncnf}')) / float(et) * 60
                await channel.send(f'<@{message.author.id}>, {et}초, {round(al, 2)}타')

            elif message.content == '준홍아 주사위':
                dice = random.randint(1, 6)
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value=(dice), inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 규카츠':
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA0MDlfOTgg%2FMDAxNTIzMjQ4NTQxOTgy.27rWawoPnQujw6HS4nPxcYjsbdZYnq-Ml3w0Q9DA3ggg.ECeoJu1W2ZiaWM8GvnPKGUylujeSjddKzkVMHZ1MuSYg.JPEG.creamy0080%2F12.%25B4%25EB%25C0%25FC%25C1%25DF%25BE%25D3%25BF%25AA%25B8%25C0%25C1%25FDDSC03358..jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 짜장면':
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="http://post.phinf.naver.net/MjAxNzEyMDVfMTgx/MDAxNTEyNDUzODM1Nzgz.oLCRrLmG048QINV4T7flJ1n5whWnMgXe2FPzjD8wvMog.1fVLRKcFZlnTg3DYFO8wrGnW9wZyZpx7Yd8hkGG3RTsg.JPEG/IIh6-J6mXMeGwnXBKX2yJP5ooR_0.jpg")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 냉면':
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="http://post.phinf.naver.net/MjAxODA2MDdfMzUg/MDAxNTI4MzUyNjUzMDE1.ZA0IG7V1Ghd2c1FAp1JPvH__g8kKncVHOOYj8wkEFn4g.xGGLSjvb4a4Pqu35ghIEh7WhCwRzxm80BWxNo9q1U3Ig.JPEG/I-5vjeJnAa7azL8tI3ihsiYYU6oQ.jpg")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 개발코드':
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value='파이썬으로 개발됬어요!', inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 닉네임':
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value=f"{message.author.display_name} 입니다.", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith('준홍아 청소'):
                if message.author.id in owner:
                    # if message.author.guild_permissions.administrator:
                    varrr = message.content.split(' ')
                    await message.channel.purge(limit=int(varrr[2]) + 1)
                    msg = await message.channel.send(
                        embed=discord.Embed(title=f'메시지 {str(int(varrr[2]))}개 삭제 완료!', descirption='응용 기능',timestamp=message.created_at, colour=discord.Colour.blue()).set_footer(icon_url=message.author.avatar_url, text=f'{str(message.author)}, 인증됨'))
                    await asyncio.sleep(3)
                    await msg.delete()
                else:
                    await channel.send("당신은 권한이 없습니다")



            elif message.content.startswith("준홍아 cmd"):
                if message.author.id in owner:
                    try:
                        a = message.content[8:]
                    except:
                        await message.channel.send("내용을 입력해주세요!")
                        return
                    proc = await asyncio.create_subprocess_shell(a, stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
                    dd, _ = await proc.communicate()
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="cmd", value=f"{dd.decode('cp949')}", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)


            elif message.content.startswith('준홍아 정보'):
                if str(message.content[7:]) == '': #애반데..뭐가 넘 비효율적으로 잡음.. 이 주석 뭔데 지워버릴까
                    user = message.author
                    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                    status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                        discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                        discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                        discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"} # 님 어떻게 됬음??/ 고쳣는데 왜 적용이 안됨..; 저장 Autosave no? 왔? 그게 뭐꼬
                    user_status = status_dict[user.status]
                    if not len(message.author.roles) == 1:
                        roles = [role for role in user.roles]
                        embed=discord.Embed(colour=message.author.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                    else:
                        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"유저정보 - {user}")
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
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"유저정보 - {user}")
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
                                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"봇정보 - {user}")
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
                        try:
                            user = message.guild.get_member(int(message.content.split()[2].replace('<@','').replace('>','').replace("!","")))
                        except ValueError:
                            embed = discord.Embed(title="경고",description="옳바른 값을 입력해주세요",colour=0x85CFFF)
                            await channel.send(embed=embed)
                            return
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"유저정보 - {user}")
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
                                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"봇정보 - {user}")
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
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20130412_259%2Froyalrate7_1365760080337VvTgW_JPEG%2FDSCN7945.jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 감자칩':
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzEyMTJfMjA4%2FMDAxNTEzMDc4MjgwMjE5.B5xVKAl3CNo8jaYf0trsO8Wr_8XfJJRjmwn8rO6VNM0g.I5dfl1H7vyDdeK0C0xAx7cNaRyIkEYvzed3gJRhxTGgg.JPEG.changuk1225%2F%25BD%25BA%25C6%25E4%25C0%25CE_%25C6%25E4%25C0%25CE%25C6%25AE%25C5%25EB_%25B0%25A8%25C0%25DA%25C4%25A8_%25BA%25B8%25B4%25D2%25B6%25F3%25B0%25A8%25C0%25DA%25C4%25A8_5.jpg&type=b400")
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content == '준홍아 뭐해':
                a = random.randint(1, 2)
                if a == 1:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="나? 수현이랑 놀거나  준홍 괴롭히지 ㅎㅎㅎㅎ", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                if a == 2:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="준홍에게 개발 이라는 고문을 받..죄송합니다. 사실 노는중임ㅋㅋ", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            elif message.content.startswith('준홍아 밴'):  # 해피야 밴 <@657876471750066186> 나쁜 짓 해떠여
                if message.author.guild_permissions.administrator:
                    author = message.content[9:27]
                    reason = message.content[29:] + f'\n\n밴 한 사람 : {message.author}'
                    await message.guild.get_member(int(author)).ban(reason=reason)
                    await message.channel.send(f"<@{author}> 님이 밴되었어요.\n사유 : {reason}")
                    return
                else:
                    await channel.send("권한없음")


            elif message.content.startswith('준홍아 공지'):
                if message.author.id in owner:
                    msg = message.content[7:]
                    embed = discord.Embed(
                        title=msg.split('and')[0],
                        description=msg.split('and')[1] + '\n\n이 체널에 공지가 오는것이 싫다면 `봇-공지` 채널을 만들어주세요! \n\n[팀 SB 디스코드](http://discord.gg/UeWTsCg)\n[코어 엔터테인먼트](https://discord.gg/TeCpcBq)',
                        colour=discord.Colour.blue(),
                        timestamp=message.created_at
                    ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - 인증됨').set_thumbnail(
                        url=client.user.avatar_url)
                    for i in client.guilds:
                        arr = [0]
                        alla = False
                        z = 0
                        for j in i.channels:
                            arr.append(j.id)
                            z += 1
                            if "봇-공지" in j.name or "봇_공지" in j.name or "bot_announcement" in j.name or j.name in '『준홍봇ㆍ공지방』' or "봇공지" in j.name:
                                if str(j.type) == 'text':
                                    try:
                                        await j.send(embed=embed)
                                        alla = True

                                    except:
                                        pass
                                    break
                        if alla == False:
                            try:
                                chan = i.channels[1]
                            except:
                                pass
                            if str(chan.type) == 'text':
                                try:
                                    await chan.send(embed=embed)
                                except:
                                    pass
                    await channel.send("완료")
                else:
                    await channel.send("NO 권한")
                    return

            elif message.content.startswith("준홍아 eval"):
                if message.author.id in owner:
                    a = message.content[9:]

                    # if message.content in ['output','token', 'file=', 'os', 'logout', 'login', 'quit', 'exit', 'sys', 'shell', 'dir']:
                    # embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    # embed.add_field(name="준홍봇 안내기능", value=f'{message.content} 그 명령어는 금지된 단어가 포함되어있습니다.', inline=True)
                    # embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    # await message.channel.send(embed=embed)
                    # return None

                    try:
                        msg = await message.channel.send(
                            embed=discord.Embed(color=0x85CFFF, title="evaling...", description=f"""📥INPUT📥
    ```
    {a}
    ```
    📤OUTPUT📤
    ```py
    evaling...
    ```"""))
                        aa = await eval(a)
                    except Exception as e:
                        await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval", description=f"""📥INPUT📥
    
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
                            await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval", description=f"""📥INPUT📥
    
    ```
    {a}
    ```
    📤OUTPUT📤
    ```py
    {e}
    ```"""))
                        else:
                            await msg.edit(embed=discord.Embed(color=0x85CFFF, title=f"eval", description=f"""📥INPUT📥
    ```
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```"""))
                    else:
                        await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval", description=f"""📥INPUT📥
    ```
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```"""))
                else:
                    await channel.send("권한없음")

            elif message.content == "준홍아 stop":
                if message.author.id in owner:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 관리기능", value="정지중....", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    os.system("pause")

            elif message.content == "준홍아 reboot":
                if message.author.id in owner:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 관리기능", value="재시작중....", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                    await client.close()
                    os.system("py V4_1.py")

            elif message.content == '준홍아 현재시각':
                now = time.localtime()
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="%02d시%02d분%02d초" % (now.tm_hour, now.tm_min, now.tm_sec),inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

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
                embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 채팅기능", value="ㅇㅇ 켜짐", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await channel.send(embed=embed)

            elif message.content.startswith("준홍아 계산"):
                channel = message.channel
                math = message.content[7:]
                if math == "":
                    await message.channel.send('계산식를 입력해주세요')
                elif len(message.mentions) >= 1 or len(message.role_mentions) >= 1 or len(
                        message.channel_mentions) >= 1:
                    await message.channel.send('계산식이 올바르지 않습니다..')
                else:
                    mathtext = ""
                    allowed = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "*", "**", "x", "X", "^", "/", "(", ")", "%"]
                    for i in math:
                        if i in allowed:
                            mathtext += i
                        else:
                            mathtext += ""
                    try:
                        value = eval(mathtext)
                        embed = discord.Embed(
                            title=f'{mathtext} 식의 결과',
                            description=f'{str(value)}',
                            colour=0x85CFFF
                        )
                        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                        await channel.send(embed=embed)
                    except:
                        await channel.send("계산식이 올바르지 않습니다..")

            elif message.content == '준홍아 애교해봐':
                p = random.randint(1, 3)
                if p == 1:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="하고싶지 않습니다", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                if p == 2:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="1더하기 1은 기요미", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                if p == 3:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name="준홍봇 채팅기능", value="낙으로 보냈습니다.", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

            else:
                m = random.randint(1, 2)
                if m == 1:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name=":no_entry_sign: 명령어 안내 :no_entry_sign:", value="그게 무슨 명령어야?", inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)
                if m == 2:
                    embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                    embed.add_field(name=":no_entry_sign: 명령어 안내 :no_entry_sign:",value=f'{message.content} 이/라는 명령어는 없어', inline=True)
                    embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

    except Exception as ex:
        embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        embed.add_field(name=":no_entry_sign: 오류!! ERROR!! :no_entry_sign:", value=f'에러 준홍봇에서 발생해요!\n에러에 대한 내용이 팀 SB에게 전송되었습니다!\n에러 내용 : {str(ex)} 사용방법이 궁금하시다면 `준홍아 도움`',inline=True)
        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
        await channel.send(embed=embed)
        embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        embed.add_field(name="에러발생!", value=f'guild : {message.channel.guild}({message.guild.id})\nch = {message.channel.name}({message.channel.id})\nauthor = {message.author}({message.author.id})\ncontent = {message.content}\nerror = {str(ex)}',inline=True)
        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
        await client.get_channel(int(errorchannel)).send(embed=embed)

access_token = "token"
#access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
