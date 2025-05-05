# handlers/torcida.py

from telegram import Update
from telegram.ext import ContextTypes
import random

torcidas = [
    "🔥 VAMO FURIA! Rumo ao topo!",
    "💣 A Fúria vai explodir tudo no servidor!",
    "🧠 Estratégia, mira e coração! Vai pra cima, FURIA!",
    "🎯 Cada round é nosso, não para!",
    "🐆 A selva é nossa! FURIAAAA!",
]

async def send_cheer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    mensagem = f"🎉 {user} grita da arquibancada:\n\n{random.choice(torcidas)}"
    await update.message.reply_text(mensagem)

async def group_cheer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if any(palavra in texto for palavra in ["furia", "vamo", "vamos", "go furia", "força", "fúria"]):
        await update.message.reply_text("🔥 A torcida tá pegando fogo aqui no grupo! VAMO FURIA!")
