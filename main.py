import asyncio
import datetime
import nest_asyncio
from io import BytesIO
from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode
import os
from dotenv import load_dotenv

# ✅ .env 파일 로드
load_dotenv()

nest_asyncio.apply()

# ✅ 환경변수에서 값 불러오기
BOT_TOKEN = os.getenv("8490843979:AAGmlhJEqSA-6wTpBNZ3neaWdHwt64TQy9M")
TARGET_CHAT_ID = os.getenv("-1002518172704")
GIF_PATH = os.getenv("private.mp4")


with open(GIF_PATH, "rb") as f:
    gif_bytes = f.read()

MESSAGE = """
▫️<a href="https://t.me/c/2518172704/5257">구인</a>▫️<a href="https://t.me/c/2518172704/5257">구직</a>▫️<a href="https://t.me/c/2518172704/5257">모집</a>▫️
▫️<a href="https://t.me/c/2518172704/5258">토토</a>▫️<a href="https://t.me/c/2518172704/5258">카지노</a>▫️<a href="https://t.me/c/2518172704/5258">홀덤</a>▫️
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2518172704/5259">코인대행</a>▫️<a href="https://t.me/c/2518172704/5259">OTC업체</a>▫️<a href="https://t.me/c/2518172704/5259"> </a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2518172704/5260">종합</a>▫️<a href="https://t.me/c/2518172704/5260">마케팅</a>▫️<a href="https://t.me/c/2518172704/5260">홍보관련</a>
▫️<a href="https://t.me/c/2518172704/5261">디자인</a>▫️<a href="https://t.me/c/2518172704/5261">포토샾</a>▫️<a href="https://t.me/c/2518172704/5261">영상</a>
▫️<a href="https://t.me/c/2518172704/5262">인증</a>▫️<a href="https://t.me/c/2518172704/5262">국내/해외</a>▫️<a href="https://t.me/c/2518172704/5262">계정</a>
▫️<a href="https://t.me/c/2518172704/5263">텔레그램</a>▫️<a href="https://t.me/c/2518172704/5263">전문</a>▫️<a href="https://t.me/c/2518172704/5263">업자</a>
▫️<a href="https://t.me/c/2518172704/5264">상위노출</a>▫️<a href="https://t.me/c/2518172704/5264">SEO</a>▫️<a href="https://t.me/c/2518172704/5264">트레픽</a>
▫️<a href="https://t.me/c/2518172704/5265">대리결제</a>▫️<a href="https://t.me/c/2518172704/5265">카드결제</a>▫️<a href="https://t.me/c/2518172704/5265"> </a>
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
▫️<a href="https://t.me/c/2518172704/5266">웹개발</a>▫️<a href="https://t.me/c/2518172704/5266">솔루션</a>▫️<a href="https://t.me/c/2518172704/5266">프로그램</a>
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

BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("📘 운영정책", url="https://t.me/privateO2C"),
        InlineKeyboardButton("💰 에스크로", url="https://t.me/privatePrimeOTC")
    ],
    [
        InlineKeyboardButton("✉️ private건의사항", url="https://t.me/privatebot12")
    ]
])

# ▶️ "업자" 정확히 입력한 경우에만 발송
async def keyword_trigger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.strip() == "업자":
        gif_io = BytesIO(gif_bytes)
        gif_io.name = "private.mp4"
        await context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=gif_io,
            caption=MESSAGE,
            parse_mode=ParseMode.HTML,
            reply_markup=BUTTONS
        )

# 주기적 전송 루프
async def send_loop(bot: Bot):
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
                    parse_mode=ParseMode.HTML,
                    reply_markup=BUTTONS
                )
            print(f"✅ [{now}] 메시지 전송 완료")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
        await asyncio.sleep(18000)  # 5시간

# 메인 실행
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), keyword_trigger))
    bot = Bot(token=BOT_TOKEN)
    asyncio.create_task(send_loop(bot))
    print("📡 봇 폴링이 시작되었습니다")
    await app.run_polling()

# 실행부 (Python 3.12 대응)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
