# handlers/news.py

from telegram import Update
from telegram.ext import ContextTypes

async def send_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    noticias = [
        "🔫 FURIA vence a NAVI em uma virada histórica!",
        "🔥 Novo jogador anunciado para o elenco de CS2!",
        "🎯 FURIA se classifica para os playoffs da IEM Katowice!",
        "🧠 Entrevista exclusiva com o arT sobre estratégias recentes.",
    ]

    mensagem = "📰 Últimas notícias da FURIA:\n\n"
    mensagem += "\n".join(f"• {n}" for n in noticias)

    await update.message.reply_text(mensagem)
