# handlers/profile.py
import sqlite3

def show_profile(update, context):
    """Exibe perfil do usuário."""
    user_id = update.effective_user.id
    # Exemplo de consulta: recuperar pontuação e mensagens do DB
    conn = sqlite3.connect('data/users.db')
    cur = conn.cursor()
    cur.execute("SELECT quiz_score, support_count FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    if row:
        score, count = row
        update.message.reply_text(f"🎉 Seu perfil:\nQuiz Score: {score}\nMensagens de apoio enviadas: {count}")
    else:
        update.message.reply_text("Perfil não encontrado. Jogue o quiz ou envie mensagens para criar seu perfil!")
    conn.close()
