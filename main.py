import asyncio
import datetime
from telegram import Bot
from telegram.constants import ParseMode

BOT_TOKEN = "8490843979:AAGmlhJEqSA-6wTpBNZ3neaWdHwt64TQy9M"
TARGET_CHAT_ID = "@여기에_대상_채널이나_그룹_아이디_입력"
GIF_PATH = "private.gif"

MESSAGE = """
▫️<a href="https://t.me/c/2694135929/17">구인</a>▫️<a href="https://t.me/c/2694135929/17">구직</a>▫️<a href="https://t.me/c/2694135929/17">모집</a>▫️
▫️<a href="https://t.me/c/2694135929/17">토토</a>▫️<a href="https://t.me/c/2518172704/5258">카지노</a>▫️<a href="https://t.me/c/2694135929/17">홀덤</a>▫️
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2694135929/17">코인대행</a>▫️<a href="https://t.me/c/2518172704/5259">OTC업체</a>▫️<a href="https://t.me/c/2694135929/17"> </a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2694135929/17">종합</a>▫️<a href="https://t.me/c/2518172704/5260">마케팅</a>▫️<a href="https://t.me/c/2694135929/17">홍보관련</a>
▫️<a href="https://t.me/c/2694135929/17">디자인</a>▫️<a href="https://t.me/c/2518172704/5261">포토샾</a>▫️<a href="https://t.me/c/2694135929/22">영상</a>
▫️<a href="https://t.me/c/2694135929/17">인증</a>▫️<a href="https://t.me/c/2518172704/5262">국내/해외</a>▫️<a href="https://t.me/c/2694135929/17">계정</a>
▫️<a href="https://t.me/c/2694135929/17">텔레그램</a>▫️<a href="https://t.me/c/2518172704/5263">전문</a>▫️<a href="https://t.me/c/2694135929/17">업자</a>
▫️<a href="https://t.me/c/2694135929/17">상위노출</a>▫️<a href="https://t.me/c/2518172704/5264">SEO</a>▫️<a href="https://t.me/c/2694135929/17">트레픽</a>
▫️<a href="https://t.me/c/2694135929/17">대리결제</a>▫️<a href="https://t.me/c/2518172704/5265">카드결제</a>▫️<a href="https://t.me/c/2694135929/26"> </a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2694135929/17">웹개발</a>▫️<a href="https://t.me/c/2518172704/5266">솔루션</a>▫️<a href="https://t.me/c/2694135929/17">프로그램</a>
▫️<a href="https://t.me/c/2518172704/5267">유심</a>▫️<a href="https://t.me/c/2518172704/5267">라우터</a>▫️<a href="https://t.me/c/2518172704/5267">에그</a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2518172704/5268">유입전문</a>▫️<a href="https://t.me/c/2518172704/5268">퍼미션</a>▫️<a href="https://t.me/c/2518172704/5268">콜센터</a>
▫️<a href="https://t.me/c/2518172704/5269">국내문자</a>▫️<a href="https://t.me/c/2518172704/5269">해외문자</a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2518172704/5270">웹해킹</a>▫️<a href="https://t.me/c/2518172704/5270">추출</a>▫️<a href="https://t.me/c/2518172704/5270">디도스</a>
▫️<a href="https://t.me/c/2518172704/5271">각종DB</a>▫️<a href="https://t.me/c/2518172704/5271">업자</a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2518172704/5272">세탁</a>▫️<a href="https://t.me/c/2518172704/5272">환전</a>▫️<a href="https://t.me/c/2518172704/5272">가상</a>▫️<a href="https://t.me/c/2518172704/5272">PG</a>
▫️<a href="https://t.me/c/2518172704/5273">장매입/판매/장묶</a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2518172704/5274">유흥사이트</a>▫️<a href="https://t.me/c/2518172704/5274">토렌트</a>
▫️<a href="https://t.me/c/2518172704/5275">TV</a>▫️<a href="https://t.me/c/2518172704/5275">영화</a>▫️<a href="https://t.me/c/2518172704/5275">애니</a>▫️<a href="https://t.me/c/2518172704/5275">중계</a>
▫️<a href="https://t.me/c/2518172704/5276">명품</a>▫️<a href="https://t.me/c/2518172704/5276">레플리카</a>▫️<a href="https://t.me/c/2518172704/5276">주얼리</a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2518172704/5278">기타업자</a>
▫️<a href="https://t.me/c/2518172704/5279">private</a>▫️<a href="https://t.me/c/2518172704/5279">동맹제휴</a>
"""

async def send_loop():
    bot = Bot(token=BOT_TOKEN)
    print("✅ 봇 실행됨 - 5시간 간격 메시지 전송 시작")

    while True:
        try:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"📤 [{now}] 메시지 전송 중...")

            with open(GIF_PATH, 'rb') as gif:
                await bot.send_animation(
                    chat_id=TARGET_CHAT_ID,
                    animation=gif,
                    caption=MESSAGE,
                    parse_mode=ParseMode.HTML
                )

            print(f"✅ [{now}] 메시지 전송 완료")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")

        await asyncio.sleep(18000)  # 5시간

if name == "main":
    asyncio.run(send_loop())
