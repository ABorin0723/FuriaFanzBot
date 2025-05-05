# handlers/quiz.py

from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
import sqlite3

QUIZ = 1

questions = [
    {"question": "Em que ano a FURIA foi fundada?", "answer": "2017"},
    {"question": "Qual o apelido do jogador Andrei Piovezan?", "answer": "arT"},
    {"question": "Quantos jogadores tem um time de CS:GO competitivo?", "answer": "5"},
]

async def quiz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["score"] = 0
    context.user_data["current_q"] = 0
    await update.message.reply_text("🎮 Quiz FURIA iniciado!\n\n" + questions[0]["question"])
    return QUIZ

async def quiz_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_answer = update.message.text.strip().lower()
    q_index = context.user_data["current_q"]
    correct_answer = questions[q_index]["answer"].lower()

    if user_answer == correct_answer:
        context.user_data["score"] += 1
        await update.message.reply_text("✅ Correto!")
    else:
        await update.message.reply_text(f"❌ Errado! Resposta certa: {questions[q_index]['answer']}")

    context.user_data["current_q"] += 1

    if context.user_data["current_q"] < len(questions):
        next_q = questions[context.user_data["current_q"]]["question"]
        await update.message.reply_text(f"👉 Próxima:\n{next_q}")
        return QUIZ
    else:
        score = context.user_data["score"]
        await update.message.reply_text(f"🏁 Fim do quiz! Você acertou {score} de {len(questions)}.")

        # Salva no banco
        conn = sqlite3.connect("data/users.db")
        cur = conn.cursor()
        user_id = update.effective_user.id
        cur.execute("INSERT OR IGNORE INTO users (user_id, quiz_score, support_count) VALUES (?, 0, 0)", (user_id,))
        cur.execute("UPDATE users SET quiz_score = quiz_score + ? WHERE user_id = ?", (score, user_id))
        conn.commit()
        conn.close()

        return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Quiz cancelado.")
    return ConversationHandler.END

def quiz_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('quiz', quiz_start)],
        states={QUIZ: [MessageHandler(filters.TEXT & ~filters.COMMAND, quiz_response)]},
        fallbacks=[CommandHandler('cancel', cancel)],
    )

