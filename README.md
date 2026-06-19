# 🐶 Pit Bot

Pit Bot é um bot para Discord desenvolvido em Python utilizando `discord.py`.

Quando um novo membro entra no servidor, o Pit Bot decide aleatoriamente se gostou ou não da pessoa e envia uma mensagem de boas-vindas acompanhada de uma imagem de um pitbull. Quando alguém sai do servidor, o bot anuncia sua partida para os demais membros.

## Funcionalidades

* ✅ Detecta entrada de novos membros
* ✅ Envia mensagem personalizada de boas-vindas
* ✅ Escolhe aleatoriamente entre uma recepção amigável ou ameaçadora
* ✅ Envia imagem junto da mensagem
* ✅ Detecta quando um membro sai do servidor
* ✅ Utiliza variáveis de ambiente para proteger o token do bot

## Tecnologias Utilizadas

* Python 3.11+
* discord.py
* python-dotenv

## Estrutura do Projeto

```text
.
├── app.py
├── pitbull-boxing.png
├── requirements.txt
├── .env
└── .gitignore
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/pitbot.git
cd pitbot
```

Crie e ative um ambiente virtual:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
BOT_TOKEN=SEU_TOKEN_DO_DISCORD
```

## Executando o Bot

```bash
python app.py
```

Se tudo estiver correto, o terminal exibirá:

```text
AAAAAAAAUUUUUUUUUHHHHH!!!!!!
```

## Comportamento

### Entrada de Membros

Quando um usuário entra no servidor, o bot escolhe aleatoriamente uma das opções:

**Pit Bot não gostou:**

```text
@usuario chegou! O Pit Bot não gostou de Usuario 😡
```

**Pit Bot gostou:**

```text
@usuario chegou! O Pit Bot gostou de Usuario 👍
Você está seguro por enquanto...
```

Além da mensagem, uma imagem de pitbull é enviada ao canal.

### Saída de Membros

Quando alguém sai do servidor:

```text
@usuario abandonou o território dos Pits...
```

## Variáveis de Ambiente

| Variável  | Descrição            |
| --------- | -------------------- |
| BOT_TOKEN | Token do bot Discord |

## Dependências

As dependências do projeto estão listadas em `requirements.txt` e incluem:

* discord.py
* python-dotenv
* aiohttp
* aiosignal
* attrs
* frozenlist
* multidict
* yarl

## Autor

Desenvolvido por João Henrique como projeto de estudo utilizando Python e Discord API.
