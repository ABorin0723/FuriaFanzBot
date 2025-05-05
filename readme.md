
# 🤖 FURIA Bot – Telegram Fan Experience

Um bot de Telegram criado para fãs do time de CS:GO da FURIA, oferecendo uma experiência completa de interação com o time, incluindo notícias, jogos ao vivo, torcida interativa e quizzes personalizados.

---

## 🚀 Funcionalidades

- `/start` – Mensagem de boas-vindas e menu interativo com botões  
- `/live` – Mostra jogos ao vivo ou os próximos da FURIA  
- `/news` – Últimas notícias sobre a equipe  
- `/quiz` – Inicia um quiz sobre a FURIA  
- `/torcida` – Envia mensagens de torcida personalizadas  
- `/profile` – Ainda não funciona  
- `/store` - Ainda não funciona  

---

## 🧰 Tecnologias Utilizadas

- Python 3.11+  
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
- SQLite (banco de dados local)  
- [hltv_async_api](https://pypi.org/project/hltv-async-api/) – para jogos ao vivo  
- `.env` para variáveis de ambiente  

---

## 📦 Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/furia-bot.git
cd furia-bot
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
venv\Scripts ctivate  # No Windows
# ou
source venv/bin/activate  # No Linux/macOS
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

> Obs: caso utilize funcionalidades com `JobQueue`, você pode instalar com:
```bash
pip install "python-telegram-bot[job-queue]"
```

4. **Configure o arquivo `.env`:**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
BOT_TOKEN=SEU_TOKEN_AQUI
```

Substitua `SEU_TOKEN_AQUI` pelo token do seu bot gerado com o [BotFather](https://t.me/BotFather).

---

## 🧠 Banco de Dados

O banco de dados é criado automaticamente ao iniciar o bot. Ele utiliza SQLite (`database.db`) e armazena perfis de usuários e pontuações do quiz.

---

## ▶️ Como Rodar

Após configurar o `.env` e instalar as dependências:

```bash
python main.py
```

O terminal ficará “parado”, aguardando mensagens no Telegram. Isso significa que o bot está **rodando**.

---

## 📱 Interagindo com o Bot

1. Abra o Telegram.  
2. Acesse o seu bot através do link: `https://t.me/seu_bot_username` (substitua pelo seu @).  
3. Use comandos como `/start`, `/quiz`, `/news`, etc.

---

## 🛠️ Estrutura do Projeto

```
furia-bot/
│
├── handlers/             # Comandos e lógica por funcionalidade
│   ├── live.py
│   ├── news.py
│   ├── quiz.py
│   ├── torcida.py
│   ├── profile.py
│   └── store.py
│
├── database.db           # Banco de dados SQLite (gerado automaticamente)
├── db.py                 # Funções de manipulação do banco
├── main.py               # Arquivo principal do bot
├── .env                  # Token do bot (não subir para o GitHub)
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

---

## 💡 To-Do (Melhorias Futuras)

- [ ] Ativar e finalizar `/profile` com ranking e edições  
- [ ] Finalizar `/store` com interações e compras fictícias  
- [ ] Criar painel web para estatísticas dos usuários  
- [ ] Incluir sistema de pontuação e recompensas  

---

## 🏁 Licença

Este projeto é de uso educacional e sem fins lucrativos. Sinta-se à vontade para adaptar, reutilizar e compartilhar.

🙋‍♂️ Autor
Feito por ABorin com carinho e amor pela FURIA 🖤
