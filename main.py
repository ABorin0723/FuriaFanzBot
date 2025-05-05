from telegram.ext import Application, CommandHandler, MessageHandler, filters
import datetime
from handlers import live, news, torcida, quiz, store, profile
from datetime import time
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obtém o token do bot do arquivo .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("Erro: BOT_TOKEN não encontrado. Certifique-se de que o .env está configurado corretamente.")
    exit()

# Função do comando /start
async def start(update, context):
    """Handler do comando /start"""
    await update.message.reply_text(
        f"👋 Bem-vindo(a) ao Bot da FURIA, {update.effective_user.first_name}! "
        "Estou aqui para levar você ao coração do time com placares, notícias e diversão."
    )

if __name__ == "__main__":
    # Cria a aplicação do bot com o token
    app = Application.builder().token(BOT_TOKEN).build()

    # Comandos básicos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live.send_live))  # Envia jogos ao vivo
    app.add_handler(CommandHandler("news", news.send_news))  # Envia últimas notícias
    app.add_handler(CommandHandler("torcida", torcida.send_cheer))  # Envia mensagem de torcida personalizada
    app.add_handler(CommandHandler("loja", store.show_catalog))  # Mantido, mesmo que não funcione

    # Quiz: usa ConversationHandler para fluxo de perguntas
    app.add_handler(quiz.quiz_handler())

    # Perfil do usuário
    app.add_handler(CommandHandler("perfil", profile.show_profile))

    # Exemplo: captura de mensagens em grupos para torcida
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUP, torcida.group_cheer))

    # Notificações programadas (exemplo: alerta de próximo jogo)
    job_queue = app.job_queue
    job_queue.run_daily(live.daily_match_alert, time=datetime.time(hour=18, minute=0))

    # Inicia o bot (polling)
    app.run_polling()
