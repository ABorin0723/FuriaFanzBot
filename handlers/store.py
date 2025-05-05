# handlers/store.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def show_catalog(update, context):
    """Exibe alguns produtos fictícios da loja FURIA."""
    keyboard = [
        [InlineKeyboardButton("Camiseta FURIA – Ver", url="https://loja.furia.com/camiseta")],
        [InlineKeyboardButton("Boné FURIA – Ver", url="https://loja.furia.com/bone")],
        [InlineKeyboardButton("Cupom de 10% – Usar", callback_data="coupon_10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("🛒 **Loja FURIA** - Escolha um produto ou use um cupom:", reply_markup=reply_markup, parse_mode='Markdown')

def handle_button(update, context):
    """Trata cliques dos botões inline (p. ex., cupom)."""
    query = update.callback_query
    data = query.data
    if data.startswith("coupon_"):
        discount = data.split("_")[1]
        # Gera código de cupom fictício
        coupon_code = f"FURIA{discount}"
        query.answer()
        query.edit_message_text(f"🎟️ Parabéns! Seu cupom de {discount}%: `{coupon_code}`", parse_mode='Markdown')
