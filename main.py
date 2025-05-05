# main.py
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, filters
import config
import datetime
from handlers import live, news, torcida, quiz, store, profile
from datetime import time

def start(update, context):
    """Handler do comando /start"""
    update.message.reply_text(
        f"👋 Bem-vindo(a) ao Bot da FURIA, {update.effective_user.first_name}! "
        "Estou aqui para levar você ao coração do time com placares, notícias e diversão."
    )

if __name__ == "__main__":
    # Cria a aplicação do bot
    app = Application.builder().token(config.BOT_TOKEN).build()

    # Comandos básicos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live.send_live))  # Corrigido
    app.add_handler(CommandHandler("news", news.send_news))       # Envia últimas notícias
    app.add_handler(CommandHandler("torcida", torcida.send_cheer))# Envia mensagem de torcida personalizada
    app.add_handler(CommandHandler("loja", store.show_catalog))   # Abre catálogo de loja

    # Quiz: usa ConversationHandler para fluxo de perguntas
    app.add_handler(quiz.quiz_handler())

    # Perfil do usuário
    app.add_handler(CommandHandler("perfil", profile.show_profile))

    # Exemplo: captura de mensagens em grupos para torcida
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUP, torcida.group_cheer))

    # Notificações programadas
    # Ex.: toda segunda às 18h, alerta do próximo jogo
    job_queue = app.job_queue
    job_queue.run_daily(live.daily_match_alert, time=datetime.time(hour=18, minute=0))

    # Inicia o bot (polling)
    app.run_polling()
