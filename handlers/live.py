# handlers/live.py

from telegram import Update
from telegram.ext import ContextTypes
from hltv_async_api import Hltv

async def send_live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Buscando partidas da FURIA...")

    hltv = Hltv()  # <- MOVIDO PARA DENTRO DA FUNÇÃO
    matches = await hltv.get_matches()
    furia_matches = [m for m in matches if 'FURIA' in m['team1']['name'] or 'FURIA' in m['team2']['name']]

    if not furia_matches:
        await update.message.reply_text("📭 Nenhuma partida da FURIA encontrada.")
        return

    response = "📅 Próximas partidas da FURIA:\n\n"
    for match in furia_matches:
        response += f"🆚 {match['team1']['name']} vs {match['team2']['name']}\n"
        response += f"🕒 {match['date']}\n"
        response += f"📍 Evento: {match.get('event', {}).get('name', 'Desconhecido')}\n"
        response += "--------\n"

    await update.message.reply_text(response)

async def daily_match_alert(context: ContextTypes.DEFAULT_TYPE):
    chat_id = "8118887610:AAGQZL0c9oAKRSrKwSL8s3jSEKlP39c4i-o"

    try:
        hltv = Hltv()  # <- TAMBÉM AQUI
        matches = await hltv.get_matches()
        furia_matches = [m for m in matches if 'FURIA' in m['team1']['name'] or 'FURIA' in m['team2']['name']]

        if furia_matches:
            response = "🔥 Alerta diário de partidas da FURIA:\n\n"
            for match in furia_matches:
                response += f"🆚 {match['team1']['name']} vs {match['team2']['name']}\n"
                response += f"🕒 {match['date']}\n"
                response += f"📍 Evento: {match.get('event', {}).get('name', 'Desconhecido')}\n"
                response += "--------\n"
        else:
            response = "📭 Nenhuma partida da FURIA hoje."

        await context.bot.send_message(chat_id=chat_id, text=response)

    except Exception as e:
        print("Erro ao buscar partidas:", e)
