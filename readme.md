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

## 🛠️ Instalação e Execução

1. **Clone o projeto**

```bash
git clone https://github.com/seu-usuario/furiabot.git
cd furiabot
(Opcional) Crie um ambiente virtual

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/macOS
Instale as dependências

bash
Copy
Edit
pip install -r requirements.txt
Crie o arquivo .env

Crie um arquivo chamado .env na raiz do projeto com o seguinte conteúdo:

env
Copy
Edit
BOT_TOKEN=SEU_TOKEN_DO_BOT_AQUI
Rode o bot

bash
Copy
Edit
python main.py
🗂️ Estrutura do Projeto
bash
Copy
Edit
furiabot/
│
├── handlers/             # Módulos separados por funcionalidade
│   ├── live.py
│   ├── news.py
│   ├── profile.py
│   ├── quiz.py
│   └── torcida.py
│
├── db.py                 # Setup e interação com banco de dados
├── main.py               # Inicializa o bot e registra os comandos
├── .env                  # Token do bot (NÃO SUBIR para o GitHub)
├── .gitignore
└── requirements.txt      # Dependências do projeto
🛑 Segurança
Adicione o arquivo .env ao seu .gitignore

Nunca suba seu token do bot para o GitHub

Exemplo de .gitignore:

gitignore
Copy
Edit
.env
venv/
__pycache__/
*.pyc
database.db
📄 Licença
Este projeto é livre para uso educacional e pessoal. Sinta-se à vontade para modificar e expandir.

🙋‍♂️ Autor
Feito por ABorin com carinho e amor pela FURIA 🖤
